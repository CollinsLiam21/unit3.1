#Liam Collins
#2/15/18
#countdown.py

num = int(input('Enter the starting number of countdown: '))

i = num
while i>0:
    print(i)
    i -= 1
    if i == 0:
        print('BOOM!')
