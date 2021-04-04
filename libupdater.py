import pickle

def Help():
    print("Commands:")
    print("-l   to see the list")
    print("-a   to add new values the list")
    print("-r   to remove values from the list")
    print("-e   to edit a value")
    print("-h   shows this message")

def Display():
    pass

def Add():
    pass

def Remove():
    pass

def Edit():
    pass

def Console(data):
    if data[0] == "-":
        if data[1] == "l":  Display()
        elif data[1] == "a":    Add()
        elif data[1] == "r":    Remove()
        elif data[1] == "e":    Edit()
        elif data[1] == "h":    Help()
        else:   print("Unrecognized command")

def First():
    vdict = {
        "Hydrogen Alpha": 656281,
        "Hydrogen Beta": 486133,
        "Hydrogen Gamma": 434047,
        "Hydrogen Delta": 410174,
        "Hydrogen Epsilon": 397007,
        "Hydrogen Zeta": 388905,
        "Hydrogen Eta": 383538,
        "Helium 1": 587500,
        "Helium 2": 501500,
        "Helium 3": 492100,
        "Helium 4": 472300,
        "Helium 5": 447100,
        "Helium 6": 388800,
        "Methane 1": 668000,
        "Methane 2": 619000,
        "Methane 3": 596000,
        "Methane 4": 576000,
        "Methane 5": 543000,
        "Iron-I 1": 645638,
        "Iron-I 2 (E2)": 527039,
        "Iron-I 3": 522715,
        "Iron-I 4 (b3)": 516891,
        "Iron-I 5 (b4)": 516749,
        "Iron-I 6 (c)": 495760,
        "Iron-I 7 (d)": 466814,
        "Iron-I 8": 404475,
        "Iron-I 9 (e)": 438355,
        "Iron-I 10 (G)": 430774,
        "Iron-I 11": 404581,
        "Iron-I 12": 388628,
        "Iron-I 13": 385991,
        "Iron-I 14": 382043,
        "Iron-I 15": 375823,
        "Iron-I 16": 374949,
        "Iron-I 17": 374826,
        "Iron-I 18": 374556,
        "Iron-I 19": 373713,
        "Iron-I 20": 373486,
        "Iron-I 21": 371994,
        "Iron-I 22 (N)": 358119,
        "Iron-I 23": 344061,
        "Magnesium-I 1": 654597,
        "Magnesium-I 2": 634674,
        "Magnesium-I 3 (b1)": 518360,
        "Magnesium-II 4 (b2)": 517268,
        "Magnesium-II 5 (b4)": 516732,
        "Magnesium-II 6": 448133,
        "Magnesium-I 7": 448113,
        "Magnesium-I 8": 439057,
        "Magnesium-I 9": 383829,
        "Magnesium-II 10": 383230,
        "Magnesium-II 11": 382936,
        "Calcium-I 1": 657278,
        "Calcium-I 2": 649378,
        "Calcium-I 3": 646257,
        "Calcium-I 4": 616217,
        "Calcium-I 5": 612222,
        "Calcium-I 6": 610272,
        "Calcium-I 7": 558876,
        "Calcium-I 8": 445661,
        "Calcium-I 9": 445589,
        "Calcium-I 10": 445478,
        "Calcium-I 11": 443569,
        "Calcium-I 12": 443496,
        "Calcium-I 13": 442544,
        "Calcium-I 14": 422673,
        "Calcium-II 15 (H)": 396847,
        "Calcium-II 16 (K)": 393366,
        "Calcium-II 17": 373690,
        "Calcium-II 18": 370603,
        "Calcium-II 19": 317933,
        "Calcium-II 20": 315887,
        "Sodium-I 1 (D1)": 589592,
        "Sodium-I 2 (D2)": 588995,
        "Sodium-II 3": 449087,
        "Sodium-II 4": 445523,
        "Sodium-II 5": 440512,
        "Sodium-II 6": 439281,
        "Sodium-II 7": 411370,
        "Sodium-II 8": 371107,
        "Sodium-II 9": 363127,
        "Sodium-II 10": 353305,
        "Sodium-II 11": 332769,
        "Sodium-II 12": 331804,
        "Sodium-II 13": 330496,
        "Sodium-II 14": 330298,
        "Sodium-I 15": 330237,
        "Sodium-II 16": 330135,
        "Sodium-II 17": 328560,
        "Sodium-II 18": 309273
    }
    file_to_write = open("library.pickle", "wb")
    pickle.dump(vdict, file_to_write)
    print('done')

if __name__ == '__main__':
    First()