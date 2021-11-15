#Q6: What is the time complexity of
p=0
for i in range(1,11):
    p=p+i
    if p>12:
        break
    print(p)


#O(n(n-1)/2)
#La complejidad es O(n^1/2)