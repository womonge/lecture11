def sumnum(num1,num2):

    x=range(num1,num2+1)

    return sum(x)

def mainsum():

    a=50
    b=150
    sumnum(a,b)

    print("Sum of number from 50 to 150 " ,(a,b,sumnum(a,b)))

mainsum()

