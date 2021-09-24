def sovpadenie(x, y, z):
    if x == y and y == z:
        return 3
    if x == y and y != z:
        return 2
    if x == z and x != y:
        return 2
    if y == z and y != x:
        return 2
    if x != y and y != z:
        return 0

a = int(input())
b = int(input())
c = int(input())
print( sovpadenie(a, b, c) )