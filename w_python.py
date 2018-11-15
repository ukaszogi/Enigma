wybór = [0, 0, 0]
rotor = [
[],
[],
[],
[],
[]
]
try:
  wybór[0] = int(imput("Podaj numer 1, rotora: "))
  wybór[1] = int(imput("Podaj numer 2, rotora: "))
  wybór[2] = int(imput("Podaj numer 3, rotora: "))
except ValueError as err:
  print(err)
  
