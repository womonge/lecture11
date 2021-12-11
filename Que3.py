def sumnum(x, y, z):

    sum = 0

    for i in range(x, y + 1):
        sum += z ** i
    return sum


def mainsum():
    x = 50
    y = 150
    z = 2
    print("sum of %d power of numbers from  %d to %d = %d" % (z, x, y, sumnum(x, y, z)))


mainsum()
