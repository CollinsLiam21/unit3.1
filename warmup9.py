#Liam Collins
#3/1/18
#warmup9.py

text = input('Enter text: ')
for ch in text:
    if ch == 'i' or ch == 'o' or ch == 'e' or ch == 'a' or ch == 'u':
        print(ch.upper())
    else:
        print(ch)
