#Liam Collins
#3/5/18
#quiz3.py

i = -15
while i<=-9:
    print(i)
    i+=1

for i in range(50,17,-4):
    print(i)
    
total = 0
for i in range(-100,1001,2):
    total = total + i
print(total)

while True:
    text = input('Enter text: ')
    if 'alpaca' in text:
        break 
    
