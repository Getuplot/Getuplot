import random
randomlist = []
maxcisel = 5
for i in range(maxcisel):
   n = random.randint(1,30)
   randomlist.append(n)
print("Vygenerované pole hodnot:", randomlist)
max_value = max(randomlist)
max_index = randomlist.index(max_value)
print("Index, kde se nachází nejvyšší hodnota:", max_index)
randomlist[max_index], randomlist[maxcisel-1] = randomlist[maxcisel-1], randomlist[max_index]
print("Nové pole: Vyměněna největší hodnota s hodnotou, která má největší index", randomlist)
