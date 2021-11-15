#Complejidad
def twoSum(array):
#la complejidad seria BigO(n^2)
#reccoren ambos array por completo
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if(i==j and array[i]+array[j]==10):
                return True
    return False
numbers=[3, 9, 8, 6]
a=twoSum(numbers)
print(a)
