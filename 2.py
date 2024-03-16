def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


alist =
alist = [int(x) for x in alist]
b=[]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
with open ('C:/Users/kids01/Desktop/Чемерисов Фёдор Алексеевич 1537/Вариант 1/songs.csv',encoding='utf-8') as f:
    title=f.readline()
    a=f.readlines()
    for i in a:
        p=i.split(';')
        k=p[4].split('.')
        b.append(k[2])