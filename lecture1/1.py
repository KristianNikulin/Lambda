def trichisla(x, y, z):
    if y < x and z < x:  
        if y < z:
            return y
        else:
            return z
    if x < y and z < y:  
        if x < z:
            return x
        else:
            return z
    if y < z and x < z:  
        if y < x:
            return y
        else:
            return x
a = int(input())
b = int(input())
c = int(input())
print( trichisla(a, b, c) )