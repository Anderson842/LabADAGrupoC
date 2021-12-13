def solution(A, B):
    # write your code in Python 3.6
    if len(A)==0 or len(B)==0:
        return 0
    ni=0
    c=1
    for i in range(1,len(A)):
        if A[i]>B[ni]:
            c+=1
            ni=i
    return c