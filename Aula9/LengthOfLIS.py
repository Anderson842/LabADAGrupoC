#LenghtOfLIS
import bisect
def lengthOfLIS(array):
    #Devuelve el tamaño de el arreglo auxiliar tmp
        tmp=[]        
        for n in array:
            x=bisect.bisect_left(tmp,n)
            if x==len(tmp):
                tmp.append(n)
            elif tmp[x]>n:
                tmp[x]=n
        return len(tmp)
    

array=[10,9,2,5,3,7,101,18]
val= lengthOfLIS(array)
print(val)