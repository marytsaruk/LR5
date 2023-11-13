file = open("text.txt", "r")
read_text = file.read()
print(read_text) 
file_text = read_text.split()

text = {}

for word in file_text:
    word = word.strip('.,?!(){}[]\'"')
    word = word.lower()
    if word in text:
        text[word] += 1
    else:
        text[word] = 1

while True:
    print('\n Меню:')
    print('1. Кількість появ кожного слова у тексті')
    print('2. Виведення списку всіх слів')
    print('3. Завершити програму')
    choose = input('Ваш вибір: ')
    if choose == str(1):
        for word, count in text.items():            #список
            print(f'{word}: {count}')               
    elif choose == str(2):
        print(file_text)
    elif choose == str(3):
        print('До побачення')
        exit()
    else:
        print('Виникла помилка при введенні, спробуйте знову')        