#Encontrar el menor valor en un array
#con busqueda binaria

def menor (array):
    l=0
    r=len(array)-1
    while l<=r:
        mid = l+(r-l)//2
        if array[mid] > array[r]:
            l=mid+1
        if array[mid]< array[r]:
            r=mid
        if r==l or mid==0:
            return array[r]
        


nums=[15,18,25,35,1,3,12]
print(menor(nums))