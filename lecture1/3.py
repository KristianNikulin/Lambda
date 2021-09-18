a = []
summ = 0
for i in range(1, 11):
    a.append( int(input()) )
for i in range(len(a)):
    summ += a[i]
print(summ)