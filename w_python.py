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
[7 , 11, 2 , 8 , 17, 18, 20, 24, 4 , 25, 16, 14, 9 , 19, 6 , 22, 10, 5 , 15, 13, 23, 21, 1 , 26, 3 , 12],
[20, 1 , 16, 21, 10, 8 , 11, 3 , 13, 7 , 15, 12, 22, 5 , 9 , 19, 26, 24, 25, 14, 2 , 17, 6 , 18, 4 , 23],
[24, 21, 12, 9 , 15, 10, 20, 4 , 26, 1 , 11, 5 , 18, 17, 8 , 6 , 13, 3 , 23, 25, 2 , 19, 16, 7 , 14, 22],
[22, 10, 7 , 26, 16, 19, 17, 11, 5 , 8 , 3 , 9 , 14, 13, 24, 12, 21, 15, 20, 6 , 4 , 1 , 25, 23, 18, 2 ],
[22, 21, 26, 3 , 11, 4 , 7 , 15, 17, 18, 5 , 10, 6 , 2 , 25, 13, 24, 23, 20, 9 , 19, 8 , 12, 14, 16, 1 ]
]

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
    r_0_w = numery.get(rotor[wybór[0]][alfabet.get(tekst[l])])
    print(r_0_w)
    r_1_w = numery.get(rotor[wybór[1]][alfabet.get(r_0_w)])
    print(r_1_w)
    r_2_w = numery.get(rotor[wybór[2]][alfabet.get(r_1_w)])
    print(r_2_w)

