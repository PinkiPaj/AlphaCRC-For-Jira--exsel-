
f = open('word processing.txt', 'r', encoding="utf8")
f2 = open('result.txt', 'w', encoding="utf8")

ar = []
ar2 = []
ar3 = []
n = []
n2 = []
count = 0
#Веддите какие столбцы надо иметь в таблице. Между названиями таблицы пропишите \t и главное не забудте написать \n в конце
#Veddi what columns it is necessary to have in the table. Write \t between the table names and, most importantly, do not forget to write \n at the end
per1 = "Locale\tCore string\told loc string\tnew loc string\tmock id\n"
f2.write(per1)

for line in f:
    ar.append(line)
for i in range(len(ar)):
    count += 1
    if count > 3 and count < 5:
        ar = [line.rstrip() for line in ar]
        ar2.append(f'{(ar[i-1])[7:]}\t{(ar[i])[12:]}\t{(ar[i+1])[14:]}\t{(ar[i+2])[14:]}\t')
        ar3.append(ar[i]+ar[i+1])
    if count == 7:
        count = 0
for i in ar2:
    if i not in n:
        n.append(i)

for i in ar3:
    if i not in n2:
        n2.append(i)

for i in range(len(n2)):
    ar2=[]
    for x in range(len(ar)):
        count += 1
        if count > 3 and count < 5 and n2[i] == ar[x]+ar[x+1]:
            ar2.append((ar[x+3])[7:])
        if count == 7:
            count = 0
    c = n[i]+', '.join(ar2)
    f2.write(c + '\n')
