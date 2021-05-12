import pickle

def Load():
    file_to_read = open("library.pickle", "rb")
    loaded_dictionary = pickle.load(file_to_read)
    return loaded_dictionary

def Save(vdict):
    file_to_write = open("library.pickle", "wb")
    pickle.dump(vdict, file_to_write)

def Help():
    print("Commands:")
    print("-l   to see the list")
    print("-a   to add new values the list")
    print("-r   to remove values from the list")
    print("-e   to edit a value")
    print("-reset  resets the list")
    print("-h   shows this message")
    print("\nIf you found any bugs or have any questions ask on Github")
    print("https://github.com/G-rox-y/Spectral-Analysis-Tool\n")


def Display(vdict):
    for member in vdict:
        print(member, vdict[member])

def Add(vdict):
    try:
        element = str(input("Insert new element name: "))
        value = int(input("Insert new element wavelength in pm: "))
        vdict[element] = value
        Save(vdict)
        print(element, "added")

    except:
        print("Not a valid input, please try again")
        print("Check your spelling and lowercase/uppercase letters")
        Add(vdict)

def Remove(vdict):
    try:
        element = str(input("Insert element name: "))
        vdict.pop(element)
        Save(vdict)
        print(element, "removed")

    except:
        print("Not a valid input, please try again")
        print("Check your spelling and lowercase/uppercase letters")
        Remove(vdict)

def EditMode():
    try:
        tekst = str(input("Do you want to change the name or the value (name/value): ")).strip().lower()
        if tekst[0] == 'n': return 0
        elif tekst[0] == 'v': return 1
        else: tekst += 13

    except 1:
        print("Not a valid input, please try again")
        return EditMode()


def Edit(vdict):
    try:
        element = str(input("Insert element name: "))
        mode = EditMode()

        if not mode:
            value = vdict[element]
            vdict.pop(element)
            element2 = str(input("Insert new element name: "))
            vdict[element2] = value

        else:
            value = str(input("Insert new element value: "))
            vdict[element] = value

        Save(vdict)
        print(element, "edited")

    except:
        print("Not a valid input, please try again")
        Edit(vdict)

def Confirmed():
    print("Are you sure you want to reset the list, there is no going back, "
          "your list will return to having all default values (yes/no)")
    try:
        decision = str(input()).strip().lower()
        if decision[0] == 'y': return 1
        elif decision[0] == 'n': return 0
        else: decision += 13
    except:
        print("Not a valid input, please try again")
        return Confirmed()

def Console():
    vdict = Load()
    try:
        data = str(input("Input command: ")).strip()
        if data == "-l":  Display(vdict)
        elif data == "-a":    Add(vdict)
        elif data == "-r":    Remove(vdict)
        elif data == "-e":    Edit(vdict)
        elif data[1] == "h":    Help()
        elif data == "-reset":
            if Confirmed(): First()
            else: print("Reset canceled")
        else: print("Unrecognized command")

    except:
        print("Not a valid input, please try again")
        Console()

def First():
    vdict = {
        "Hydrogen Alpha [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 656281,
        "Hydrogen Beta [Spectral B] [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 486133,
        "Hydrogen Gamma [Spectral O] [Spectral B] [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 434047,
        "Hydrogen Delta [Spectral B] [Spectral A] [Spectral F] [Spectral G]": 410174,
        "Hydrogen Epsilon [Spectral A] [Spectral F]": 397007,
        "Hydrogen Zeta": 388905,
        "Hydrogen Eta": 383538,
        "Helium {1} (D3) [Spectral G]": 587560,
        "Helium {2}": 501500,
        "Helium {3}": 492100,
        "Helium {4}": 472300,
        "Helium II {5} [Spectral O]": 468600,
        "Helium II {6} [Spectral O] [Spectral B]": 454100,
        "Helium I {7} [Spectral O] [Spectral B]": 447100,
        "Helium I {8} [Spectral B] [Spectral A] [Spectral F]": 412100,
        "Helium {9}": 388800,
        "Methane {1}": 668000,
        "Methane {2}": 619000,
        "Methane {3}": 596000,
        "Methane {4}": 576000,
        "Methane {5}": 543000,
        "Iron I {1}": 645638,
        "Iron I {2} (E2) [Spectral G] [Spectral K]": 527039,
        "Iron I {3}": 522715,
        "Iron I {4} (b3) [Spectral G] [Spectral K]": 516891,
        "Iron I {5} (b4)": 516749,
        "Iron-I {6} (c) [Spectral G] [Spectral K]": 495760,
        "Iron I {7} (d) [Spectral G] [Spectral K]": 466814,
        "Iron I {8}": 440475,
        "Iron I {9} (e) [Spectral K]": 438355,
        "Iron I {10} (e) [Spectral G] [Spectral K]": 432500,
        "Iron I {11} (G) [Spectral G]": 430774,
        "Iron I {12} [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 430300,
        "Iron I {13} [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 429900,
        "Iron I {14}": 404581,
        "Iron I {15}": 388628,
        "Iron I {16}": 385991,
        "Iron I {17}": 382043,
        "Iron I {18}": 375823,
        "Iron I {19}": 374949,
        "Iron I {20}": 374826,
        "Iron I {21}": 374556,
        "Iron I {22}": 373713,
        "Iron I {23}": 373486,
        "Iron I {24}": 371994,
        "Iron I {25} (N)": 358119,
        "Iron I {26}": 344061,
        "Magnesium I {1}": 654597,
        "Magnesium I {2}": 634674,
        "Magnesium I {3} (b1) [Spectral G] [Spectral K]": 518360,
        "Magnesium II {4} (b2) [Spectral G] [Spectral K]": 517268,
        "Magnesium II {5} (b4) [Spectral G] [Spectral K]": 516732,
        "Magnesium II {6} [Spectral A] [Spectral F] [Spectral G]": 448133,
        "Magnesium I {7} [Spectral K]": 448113,
        "Magnesium I {8}": 439057,
        "Magnesium I {9}": 383829,
        "Magnesium II {10}": 383230,
        "Magnesium II {11}": 382936,
        "Calcium I {1}": 657278,
        "Calcium I {2}": 649378,
        "Calcium I {3}": 646257,
        "Calcium I {4}": 616217,
        "Calcium I {5}": 612222,
        "Calcium I {6}": 610272,
        "Calcium I {7}": 558876,
        "Calcium I {8}": 445661,
        "Calcium I {9}": 445589,
        "Calcium I {10}": 445478,
        "Calcium I {11}": 443569,
        "Calcium I {12}": 443496,
        "Calcium I {13}": 442544,
        "Calcium I {14} [Spectral F] [Spectral G] [Spectral K]": 422673,
        "Calcium II {15} (H) [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 396847,
        "Calcium II {16} (K) [Spectral A] [Spectral F] [Spectral G] [Spectral K]": 393366,
        "Calcium II {17}": 373690,
        "Calcium II {18}": 370603,
        "Calcium II {19}": 317933,
        "Calcium II {20}": 315887,
        "Sodium I {1} (D1) [Spectral G] [Spectral K]": 589592,
        "Sodium I {2} (D2) [Spectral G] [Spectral K]": 588995,
        "Sodium II {3}": 449087,
        "Sodium II {4}": 445523,
        "Sodium II {5}": 440512,
        "Sodium II {6}": 439281,
        "Sodium II {7}": 411370,
        "Sodium II {8}": 371107,
        "Sodium II {9}": 363127,
        "Sodium II {10}": 353305,
        "Sodium II {11}": 332769,
        "Sodium II {12}": 331804,
        "Sodium II {13}": 330496,
        "Sodium II {14}": 330298,
        "Sodium I {15}": 330237,
        "Sodium II {16}": 330135,
        "Sodium II {17}": 328560,
        "Sodium II {18}": 309273,
        "C2 (Swan) {1} [Carbon stars]": 612200,
        "C2 (Swan) {2} [Carbon stars]": 563500,
        "C2 (Swan) {3} [Carbon stars]": 516500,
        "C2 (Swan) {4} [Carbon stars]": 473800,
        "C2 (Swan) {5} [Carbon stars]": 438000,
        "C3 complex [Carbon stars]": 405600,
        "CN {1} [Carbon stars]": 421700,
        "CN {2} [Carbon stars]": 388000,
        "SiC2 Band {1} [Carbon stars]": 497700,
        "SiC2 Band {2} [Carbon stars]": 490600,
        "SiC2 Band {3} [Carbon stars]": 486700,
        "SiC2 Band {4} [Carbon stars]": 464000,
        "SiC2 Band {5} [Carbon stars]": 458100,
        "Barium II  [Carbon stars]": 455400,
        "Strontium I [Carbon stars]": 460700,
        "CH (G Band) [Spectral F] [Spectral G] [Spectral K]": 431300,
        "C III {1} [Spectral O] [Spectral B]": 465000,
        "C III {2} [Spectral B]": 454000,
        "Silicon II {1} [Spectral B] [Spectral A] [Spectral F]": 413100,
        "Silicon II {2} [Spectral B] [Spectral A] [Spectral F]": 412800,
        "Silicon IV {3} [Spectral O] [Spectral B]": 408900,
        "N III {1} [Spectral O]": 464000,
        "N III {2} [Spectral O]": 463200,
        "N III {3} [Spectral O]": 409700,
        "MgH Band [Spectral K]": 409700,
        "CaOH Band [Spectral K]": 550000,
        "{} [Spectral M]": 477500,
        "{2} [Spectral M]": 499000,
        "{3} [Spectral M]": 519000,
        "{4} [Spectral M]": 548000,
        "{5} [Spectral M]": 564000,
        "{6} [Spectral M]": 593000,
        "{7} [Spectral M]": 625000,
        "{8} [Spectral M]": 678000,
        "{9} [Spectral M]": 721000,
        "{10} [Spectral M]": 767000

    }
    Save(vdict)
    print('Reset done')

if __name__ == '__main__':
    while True:
        Console()
