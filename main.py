'''
Jeu du juste prix
'''
from random import randint
ordi=randint(1,1000)
print("Bienvenue Au Jeu du Juste Prix!")
uti=int(input("Veuillez saisir un nombre:"))
while uti!=ordi:
  if uti>ordi:
    print("c'est moins!")
    uti=int(input("Veuillez saisir un nombre:"))
  elif uti<ordi:
    print("c'est plus!")
    uti=int(input("Veuillez saisir un nombre:"))
print("C'EST GAGNER! C'était donc belle et bien {} !".format(ordi))