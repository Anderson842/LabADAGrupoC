#Complejidad
def every_other(array):
#la complejidad seria BigO(n^2)
#reccoren ambos array por completo
    for i,e in enumerate(array):
        if(i%2 ==0):
            for j in array:
                print (e,"+",j)

numbers=[3, 9, 8, 6]
a=every_other(numbers)
print(a)
