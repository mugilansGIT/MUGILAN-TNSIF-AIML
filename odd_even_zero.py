def oze(arr):
    e = z = o = 0
    for x in arr:
        if x == 0:
            z += 1
        elif x % 2 == 0:
            e += 1
        else:
            o += 1
    return e, z, o

arr = [10, 5, 0, 7, 8, 0, 13, 4]
e, z, o = oze(arr)
print(e, z, o)