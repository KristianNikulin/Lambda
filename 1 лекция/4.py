N = int(input())
a = []
col = 0
for i in range(N):
    a.append( int(input()) )
for i in range(len(a)):
    if a[i] == 0:
        col += 1
print(col)