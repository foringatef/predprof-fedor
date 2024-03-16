b=[]
while True:
    print('Введите имя артиста:')
    n=input()
    if n!='0':
        with open('C:/Users/kids01/Desktop/Чемерисов Фёдор Алексеевич 1537/Вариант 1/songs.csv', encoding='utf-8') as f:
            title = f.readline()
            a=f.readlines()
            for i in a:
                p=i.split(';')
                b.append(p[1])
                if p[1]==n:
                    print(f'У артиста {n} найдена песня {p[2]}')
                    if b.count(n) == 0:
                        print('К сожалению, ничего не удалось найти')
    else:
        break

