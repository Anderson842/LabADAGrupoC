def solution(K, A):
    # write your code in Python 3.6
    c =0
    length=0
    for i in A:
        length+=i
        if length>= K:
            c+=1
            length=0
    return c