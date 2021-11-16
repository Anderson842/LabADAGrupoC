#Q11: What is the time complexity o
p=0
x=1
for i in range(10):
    x=x*2
    if(x>9):
        break
    p+=1
    print (x)

for j in range(1,p):
    j=j*2
    if(j>p-1):
        break
    print(j)

#La complejidad es O(log n*p)