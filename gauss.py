#Liam Collins
#2/15/18
#gauss.py

start = int(input('Enter a starting number: '))
stop = int(input('Enter an ending number: '))

total = 0
for i in range(start,stop+1):
    total = total + i
print(total)

diff = int(input('Enter specific difference: '))

total = 0
for i in range (1,101,diff):
    total = total + i
print(total)

