from collections import defaultdict
from heapq import *

def BankQueue(N,T):
    for n in range(N):
        cash, time = list(map(int, input().split()))
        clientes[time].append(cash)
    temp= []
    total = 0
    for t in range(T)[::-1]:
        for price in clientes[t]:
            heappush(temp, -price)
        if temp:
            total += heappop(temp)

    return (-total)

N, T = list(map(int, input().split()))
clientes = defaultdict(list)
print(BankQueue(N,T))
