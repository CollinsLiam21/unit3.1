#Liam Collins
#2/15/18
#gauss.py

diff = int(input('Enter specific difference: '))

total = 0
for i in range (1,101):
    total = total + i
    i += diff
print(total)

