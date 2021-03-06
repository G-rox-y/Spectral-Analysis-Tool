import os
import cv2
import pickle
import numpy as np
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt
from matplotlib.widgets import Button, Slider, CheckButtons

def ImageProcesser():
    img = GetImage()
    r, g, b = GetCorrection()
    imColor = ColorCorrection(img.copy(), r, g, b)
    imBW = cv2.cvtColor(imColor, cv2.COLOR_BGR2GRAY)
    imNeg = cv2.bitwise_not(imBW)
    imFilter = Filter(imNeg)
    imClear = NoiseRemover(imFilter, imBW)
    cv2.destroyAllWindows()
    return imClear, imNeg

def SpectralIntensity(imCrop, h, w):
    # definiranje varijabli
    ylist = np.array([])
    marker = 0; scord = 0; ecord = 0

    # for petlja koja prolazi kroz svaki redak slike i zbraja mu prosječnu vrijednost
    for i in range(w):
        sum = np.int64(0)

        # zbrajanje svih vrijednosti u redu
        for j in range(h):  sum += imCrop[j][i]

        # uvjeti koji odvajaju spektar od ostatka slike
        if (marker == 0) & (sum > 0): marker = 1
        elif marker == 1 and sum == 0: marker = 2
        elif marker == 2 and sum > 0: marker = 3; scord = i
        elif marker == 3 and sum == 0: marker = 4; ecord = i

        ylist = np.append(ylist, sum)

    # lista vrijednosti x osi za spektar u pikometrima
    sran , eran = GetRange()
    xlist = Straighten(sran, eran, ecord - scord + 1)
    dif = eran - sran
    return xlist, ylist, scord, ecord, dif

def ColorCorrection(img, ammR, ammG, ammB):
    if ammR != 1.0:
        r = np.array(img[:, :, 2])
        r = r.astype(np.float16)
        r //= ammR
        r = r.astype(np.uint8)
        img[:, :, 2] = r

    if ammB != 1.0:
        b = np.array(img[:, :, 0])
        b = b.astype(np.float16)
        b //= ammB
        b = b.astype(np.uint8)
        img[:, :, 0] = b

    if ammG != 1.0:
        g = np.array(img[:, :, 1])
        g = g.astype(np.float16)
        g //= ammG
        g = g.astype(np.uint8)
        img[:, :, 1] = g

    return img

def RotationTool(image):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    #prikupljanje pozicija sa pomičnog klizača
    ang = cv2.getTrackbarPos("angle", "Cropping")
    dec = cv2.getTrackbarPos("decimal", "Cropping")
    x1 = cv2.getTrackbarPos("x1", "Cropping")
    x2 = cv2.getTrackbarPos("x2", "Cropping")
    y1 = cv2.getTrackbarPos("y1", "Cropping")
    y2 = cv2.getTrackbarPos("y2", "Cropping")
    #rotiranje matrice
    M = cv2.getRotationMatrix2D((cX, cY), ang + dec / 100, 1.0)
    #prikaz linija za rezanje slike
    rotated = cv2.warpAffine(image, M, (w, h))
    rotatedl = cv2.line(rotated, (0, y1), (w, y1), (0, 255, 0), thickness=5)
    rotatedl = cv2.line(rotatedl, (0, y2), (w, y2), (0, 255, 0), thickness=5)
    rotatedl = cv2.line(rotatedl, (x1, y1), (x1, y2), (0, 255, 0), thickness=5)
    rotatedl = cv2.line(rotatedl, (x2, y1), (x2, y2), (0, 255, 0), thickness=5)
    return rotatedl, int(x1), int(y1), int(x2), int(y2), ang+dec/100

def ImageCropping(imNeg, imClear):
    y1 = 0
    y2 = 0
    ang = float(0)
    # petlja koja osvježava izgled slike koja se reže
    while True:
        Show(RotationTool(imNeg)[0])
        # uvjet koji u slučaju pritiska slova Q spremaa promjene
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imRotate, x1, y1, x2, y2, ang = RotationTool(imClear)
            cv2.destroyAllWindows()
            break
    # rezanje slike
    if y2 < y1: y1, y2 = y2, y1
    if x2 < x1: x1, x2 = x2, x1
    imCrop = imRotate[y1:y2, x1:x2]  # gotova slika
    return imCrop

def Filter(img):
    imb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    hsv = cv2.cvtColor(imb, cv2.COLOR_BGR2HSV)
    TrackbarFilter()
    lower = np.array([0, 0, 0])
    while True:
        up = cv2.getTrackbarPos("threshold", "Filter parameters")
        upper = np.array([0, 0, up])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask= mask)
        Show(cv2.bitwise_not(result.copy()))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    return result

def NoiseRemover(src, img):
    ret, binary_map = cv2.threshold(src, 0, 255, 0)
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_map, None, None, None, 8, cv2.CV_32S)
    areas = stats[1:, cv2.CC_STAT_AREA]
    result = np.zeros(labels.shape, np.uint8)
    for i in range(0, nlabels - 1):
        if areas[i] >= 100:  # keep
            result[labels == i + 1] = 255
    #result[result == 0] = (255)
    clear = cv2.bitwise_and(img, img, mask=result)
    #que = StackImages(0.75, ([img, img], [result, clear]))
    #Show(que)
    #cv2.waitKey(0)

    return clear

def Show(img):
    imS = cv2.resize(img, (1280, 960))
    cv2.imshow('image', imS)

def Library():
    file_to_read = open("library.pickle", "rb")
    loaded_dictionary = pickle.load(file_to_read)
    return loaded_dictionary

def empty(a):
    pass

def TrackbarsCropping(shape):
    cv2.namedWindow("Cropping")
    cv2.resizeWindow("Cropping", 960, 240)
    cv2.createTrackbar("angle", "Cropping", 0, 360, empty)
    cv2.createTrackbar("decimal", "Cropping", 0, 99, empty)
    cv2.createTrackbar("x1", "Cropping", 5000, shape[1], empty)
    cv2.createTrackbar("y1", "Cropping", shape[0] // 2, shape[0], empty)
    cv2.createTrackbar("x2", "Cropping", 1300, shape[1], empty)
    cv2.createTrackbar("y2", "Cropping", shape[0] // 3, shape[0], empty)

def TrackbarFilter():
    cv2.namedWindow("Filter parameters")
    cv2.resizeWindow("Filter parameters", 960, 80)
    cv2.createTrackbar("threshold", "Filter parameters", 228, 255, empty)

def GetImage():
    Tk().withdraw()
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    return img.copy()

def GetRange():
    st = str(input("Camera wavelength lower limit(picometers): "))
    en = str(input("Camera wavelength upper limit(picometers): "))
    if st[-1] == 'z':
        start = np.int64(st[0:-1]) * 100000
        end = np.int64(en[0:-1]) * 100000
    else:
        try:
            start = np.int64(st)
            end = np.int64(en)
        except:
            print("Not a valid input, please try again")
            return GetRange()
    return start, end

def GetCorrection():
    try:
        r = np.float16(input("Red color reduction factor: "))
        g = np.float16(input("Green color reduction factor: "))
        b = np.float16(input("Blue color reduction factor: "))
    except:
        print("Not a valid input, please try again")
        return GetCorrection()
    return r, g, b

def GetMode():
    print("Linear or Logarithmic mode? (lin/log)")
    tekst = str(input())
    tekst = tekst.strip()
    tekst = tekst.lower()
    if tekst == "0": return 0
    elif tekst == "1": return 1
    elif tekst == "lin": return 0
    elif tekst == "log": return 1

    print("Not a vaild input, please try again.")
    return GetMode()

def Brusenje(values, tam, tsize):
    GData = np.array(values)
    GData2 = np.array([GData[0]])
    c = 0
    for i in range(GData.size):
        c += 1
        if c>tam:
            GDataShard = GData[c-tam:c]
            if (np.mean(GDataShard) - np.min(GDataShard) < tsize) & (np.max(GDataShard) - np.mean(GDataShard) < tsize):
                GDataShard2 = Straighten(GDataShard[0], GDataShard[tam-1], GDataShard.size + 1)
                GData2 = np.append(GData2, GDataShard2)
            else:   GData2 = np.append(GData2, GDataShard)
            if c + tam < GData.size:
                c += tam - 1
            else:
                GData2 = np.append(GData2, GData[c:GData.size + 1])
                break
    return GData2[0:GData.size]

def Straighten(start, end, size):
    change = np.float64((end - start) / (size - 2))
    arr = np.array([])
    for i in range(size - 1):   arr = np.append(arr, start + round(change * i))
    return arr

def Smoothener(values, tam, tsize):
    lista = np.array(values)
    if tam == 2: return lista
    else: lista = Brusenje(lista, tam, tsize)
    return Smoothener(lista, tam - 1, tsize)

def HoleFinder(values, xlist):
    mode = 0
    dif = 0
    holes = np.array([])
    positions = np.array([])
    for i in range(values.size):
        if i != 0:
            dif = values[i] - values[i - 1]
        if (mode == 0) & (dif < 0):
            mode = 1
        elif (mode == 1) & (dif > 0):
            mode = 0
            holes = np.append(holes, xlist[i])
            positions = np.append(positions, i)
    return holes, positions

def PlotGraph(xlist, ylist, scord, ecord, mode):
    global Slist
    global Holelist
    global Poslist

    Slist = np.array([])
    Holelist = np.array([])
    Poslist = np.array([])

    Slist = Smoothener(ylist[scord:ecord], 15, 400)
    Holelist, Poslist = HoleFinder(Slist, xlist)

    fig =plt.figure()
    ax = fig.subplots()
    plt.subplots_adjust(bottom=0.25)
    p, = ax.plot(xlist, Slist, linewidth=0.5)
    StepSlide = plt.axes([0.15, 0.15, 0.65, 0.03])
    StepFactor = Slider(StepSlide, "Step size", valmin=2, valmax=50, valinit=15, valstep=1)
    ThresholdSlide = plt.axes([0.15, 0.1, 0.65, 0.03])
    ThresholdFactor = Slider(ThresholdSlide, "Threshold", valmin=10, valmax=3000, valinit=400, valstep=5)

    ax_confirm = plt.axes([0.875, 0.125, 0.1, 0.03])
    ConfirmButton = Button(ax_confirm, "Confirm")
    if mode: ax.set_yscale('log')

    def update(val):
        global Slist
        global Holelist
        global Poslist
        currentStep = StepFactor.val
        currentThreshold = ThresholdFactor.val
        Slist = Smoothener(ylist[scord:ecord], currentStep, currentThreshold)
        Holelist, Poslist = HoleFinder(Slist, xlist)
        p.set_ydata(Slist)
        fig.canvas.draw()

    def closee(val):
        plt.close()

    StepFactor.on_changed(update)
    ThresholdFactor.on_changed(update)
    ConfirmButton.on_clicked(closee)

    def quit_figure(event):
        if event.key == 'q':
            plt.close(event.canvas.figure)

    cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)

    plt.show()

    plt.close()

    return Holelist, Poslist, Slist

def AbsorptionFinder(Holelist, Poslist, Slist, xlist, cordif, dif):
    data = pd.Series(Library())
    data.name = "Absorption line values"
    c = 0
    for part in Poslist:
        c += 1
        curr = np.int64(part)
        l = curr; r = l
        lu = True; ru = True
        lc = np.int16(0)
        rc = np.int16(0)
        while lu:
            l -= 1
            lc += 1
            if Slist[l] > Slist[l - 1]:
                lu = False
        while ru:
            r += 1
            rc += 1
            if Slist[r] > Slist[r + 1]:
                ru = False

        width = ((rc + lc) / cordif) * dif
        mby = data[(data > xlist[l + (curr - l) // 2]) & (data < xlist[curr + (r - curr) // 2])]
        print("Absorption line number ", c)
        #print("Absorption line mean witdh: ", width, "pm")
        print("Looking for variables between " + str(xlist[l + (curr - l) // 2]) + " pm, and " + str(
            xlist[curr + (r - curr) // 2]) + " pm")
        count = 0
        print(mby)
        print("--------------------------")

        i = 1
        for member in mby:
            plt.axvline(x=member, linewidth=0.3, color='green')
            plt.text(x=member, y=0, s=str(i), size=8)
            i += 1

    for part in Holelist: plt.axvline(x=part, linewidth=1, color='red')

    ax_search = plt.axes([0.45, 0.02, 0.1, 0.03])
    SearchButton = Button(ax_search, "Search")

    def closee(val):
        plt.close()

    SearchButton.on_clicked(closee)
    plt.show()
    plt.close()


def ManualDetection():
    try:
        broj = int(input("Manual detection absorption line wavelength (in pm): "))
        thr = int(input("Allowed deviation (in pm): "))

    except:
        print("Not a valid input, please try again")
        ManualDetection()
        return

    vlist = Library()
    print("--------------------------")
    print("Looking for variables between ", broj-thr, " pm, and ", broj + thr," pm")
    reslist = np.array([])
    for member in vlist:
        if abs(vlist[member] - broj) < thr:
            print(member, "-", vlist[member])
            reslist = np.append(reslist,  vlist[member])
    print("--------------------------")
    return broj, thr, reslist


def main():
    print("If the file explorer doesnt show up within a few seconds, feel free to restart the program")
    os.system('cls')

    imClear, imNeg = ImageProcesser()
    h, w = imNeg.shape[:2]
    TrackbarsCropping([h, w])
    imCrop = ImageCropping(imNeg, imClear)
    h, w = imCrop.shape[:2]

    xlist , ylist, scord, ecord, dif = SpectralIntensity(imCrop, h, w)
    xlist2 = Straighten(1, w, len(ylist) + 1)

    mode = GetMode()

    Holelist, Poslist, Slist = PlotGraph(xlist, ylist, scord, ecord, mode)
    cordif = ecord - scord

    while True:
        plt.plot(xlist, ylist[scord:ecord], linewidth=0.5)
        if mode: plt.yscale('log')
        AbsorptionFinder(Holelist, Poslist, Slist, xlist, cordif, dif)
        pos, thr, res = ManualDetection()
        plt.plot(xlist, ylist[scord:ecord], linewidth=0.5)
        plt.axvline(x=pos, linewidth=1, color='red')
        plt.axvline(x=pos+thr, linewidth=1, color='red')
        plt.axvline(x=pos-thr, linewidth=1, color='red')
        i = 0
        for part in res:
            i += 1
            plt.axvline(x=part, linewidth=1, color='green')
            plt.text(x=part, y=0, s=str(i), size=8)

        ax_search = plt.axes([0.45, 0.02, 0.1, 0.03])
        SearchButton = Button(ax_search, "Return")

        def closee(val):
            plt.close()

        SearchButton.on_clicked(closee)
        plt.show()
        plt.close()

        if mode: plt.yscale('log')
        _ = input('Enter any key to continue, or type "exit", to end the session   ')
        if _.lower().strip() == "exit": break

if __name__ == '__main__':
    main()
