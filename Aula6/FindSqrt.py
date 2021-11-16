#Verificar si un numero es cuadrado
#sin usar metodo sqrt

def findSqrt (num):
    l=0
    r=num-1
    while l<=r:
        mid = l+(r-l)//2
        if mid*mid == num:
            return True
        if mid*mid < num:
            l=mid+1
        if mid*mid > num:
            r=mid-1
    return False

print(findSqrt(14))