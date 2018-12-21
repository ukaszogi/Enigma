alfabet = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}
numery = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
}
wybór = [0, 0, 0, "", "", ""]
rotor = [
#0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
#a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
[6 , 10, 1 , 7 , 16, 17, 19, 23, 3 , 24, 15, 13, 8 , 18, 5 , 21, 9 , 4 , 14, 12, 22, 20, 0 , 25, 2 , 11],
[19, 0 , 15, 20, 9 , 7 , 10, 2 , 12, 6 , 14, 11, 21, 4 , 8 , 18, 25, 23, 24, 13, 1 , 16, 5 , 17, 3 , 22],
[23, 20, 11, 8 , 14, 9 , 19, 3 , 25, 0 , 10, 4 , 17, 16, 7 , 5 , 12, 2 , 22, 24, 1 , 18, 15, 6 , 13, 21],
[21, 9 , 6 , 25, 15, 18, 16, 10, 4 , 7 , 2 , 8 , 13, 12, 23, 11, 20, 14, 19, 5 , 3 , 0 , 24, 22, 17, 1 ],
[21, 20, 25, 2 , 10, 3 , 6 , 14, 16, 17, 4 , 9 , 5 , 1 , 24, 12, 23, 22, 19, 8 , 18, 7 , 11, 13, 15, 0 ]
]

def verdev():
    q = True
    try:
        while(q):
            q = False
            for i in range(3):
                p = True
                while(p):
                    wybór[i] = (int(input("Podaj numer "+str(i+1)+". rotora: ")) - 1)
                    if(0 <= wybór[i] <= 4):
                        p = False
                    else:
                        print("Numery rotorów to: 1, 2, 3, 4, 5")
                    if(i>0):
                        if(wybór[i]==wybór[i-1]):
                            print("Podaj inny numer rotora (rotory nie mogą się powtarzać): ")
                            p = True
                    if(i>1):
                        if(wybór[i]==wybór[i-2]):
                            print("Podaj inny numer rotora (rotory nie mogą się powtarzać): ")
                            p = True
        for j in range(3):
            j+=3
            p = True
            while(p):
                wybór[j] = str(input("Podaj literę "+str(j-3)+". rotora: ").lower())
                if(len(wybór[j])==1):
                    p = False
                else:
                    print("Podaj jedną literę")

    except ValueError:
        print("Niewłaściwy rodzaj znaku!")
        q = True

    for h in range(3):
        wybór[h+3] = int(alfabet.get(wybór[h+3]))
        print(wybór[h+3])

    r = True
    while(r):
        r = False
        tekst = str(input("Podaj tekst do szyfrowania. Bez znaków polskich i cyfr. \n\n\n").lower())
        for k in tekst:
            if(k in "1234567890ąćęłńóśźż"):
                print("Bez cyfr i polskich znaków")
                r = True 



    wynik = ""

    for l in range(len(tekst)):
        r_0_in = (alfabet.get(tekst[l])+wybór[3])%26
        print(r_0_in)
        r_0_w = numery.get(rotor[wybór[0]][r_0_in])
        print(r_0_w)
        r_1_in = (alfabet.get(r_0_w) +wybór[4])%26
        print(r_1_in)
        r_1_w = numery.get(rotor[wybór[1]][r_1_in])
        print(r_1_w)
        r_2_in = (alfabet.get(r_1_w) +wybór[5])%26
        print(r_2_in)
        r_2_w = numery.get(rotor[wybór[2]][r_2_in])
        print(r_2_w)
        wynik += r_2_w
        print(wynik)
        if(wybór[3]==25):
            wybór[3]=0
            if(wybór[4]==25):
                wybór[4]=0
                if(wybór[5]==25):
                    wybór[5]=0
                else:
                    wybór[5]+=1
            else:
                wybór[4]+=1
        else:
            wybór[3]+=1

    for h in range(3):
        print(wybór[h+3])

    print(wynik)

    
if(input("Wciśnij Enter aby zacząć...\n")=="devkod"):
    verdev()
