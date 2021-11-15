#Convertir de BigO(n^2) a BigO(n)
def greatesNumber(array):
#Covertimos usando solo un for y condicional
    mayor=0
    for i in range(0, len(array)):
        if array[i]>mayor:
            mayor=array[i]
    return mayor

numbers=[3, 9, 8, 6]
a=greatesNumber(numbers)
print(a)