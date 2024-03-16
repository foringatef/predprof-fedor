with open ('C:/Users/kids01/Desktop/Чемерисов Фёдор Алексеевич 1537/Вариант 1/songs.csv',encoding='utf-8') as f:
    title=f.readline()
    a=f.readlines()
    for i in f:
        p=i.split(';')
