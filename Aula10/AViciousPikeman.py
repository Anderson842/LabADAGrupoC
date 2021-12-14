MOD = 1000000007
def aViciousPikerman(n,time,lis):
    total_time= 0
    penalty=0
    for i,t in enumerate(lis):
        if total_time + t > time:
            return i, penalty
        total_time += t
        penalty = (penalty + total_time) % MOD
    return n, penalty

n,t = map(int,input().split())
a,b,c,t0 = map(int,input().split())
lis = [t0]
for _ in range(1,n):
    lis.append(((a*lis[-1]+b) % c) + 1)
print(*aViciousPikerman(n,t,sorted(lis)))
