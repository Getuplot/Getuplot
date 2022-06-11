import random
pole = []
pocet_hodnot = 5
for i in range(pocet_hodnot):
   n = random.randint(1,30)
   pole.append(n)
print("Vygenerované pole hodnot:", pole, "\n")

nejvyssi_cislo = pole[0]
for n in pole:
    if n>nejvyssi_cislo:
        nejvyssi_cislo = n
print("Nejvyšší číslo ze seznamu:", nejvyssi_cislo)

index_nejvyssi_hodnoty = pole.index(nejvyssi_cislo)
print("Index, kde se nachází nejvyšší hodnota (od 0):", index_nejvyssi_hodnoty, "\n")

posledni_cislo = pole[-1]
print("Poslední číslo ze seznamu:", posledni_cislo)

posledni_index = pole.index(posledni_cislo)
print("Index, kde se nachází poslední hodnota (od 0):", posledni_index, "\n")

pole[index_nejvyssi_hodnoty] = posledni_cislo
pole[posledni_index] = nejvyssi_cislo
print("Nové pole hodnot:", pole)

input()