#Encontrar el primer valor mayor o igual
#con busqueda binaria

def mayorIgual (array,num):
    l=0
    r=len(array)-1
    while l<=r:
        mid = l+(r-l)//2
        if array[mid] == num:
            return array[mid]
        if array[mid] < num:
            l=mid+1
        if array[mid] > num:
            valor=mid
            r=mid-1
    return array[valor]


nums=[2,4,6,8,12,15,18]
print(mayorIgual(nums,11))