#Complejidad
def find_needle(needle, haystack):
#la complejidad seria BigO(n^2)
#recorre ambos ciclos while
    needle_index=0
    haystack_index=0
    
    while haystack_index < len(haystack):
        if needle[needle_index]== haystack[haystack_index]:
            found_needle= True
            while needle_index < needle.length:
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
            needle_index +=1
        if found_needle:
            return True
            needle_index=0

        haystack_index +=1
    return False


numbers=[3, 9, 8, 6]
n= "efg"
h= "abcdefghijk"
a=find_needle(n,h)
print(a)
