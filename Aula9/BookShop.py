def BookShop(n,x):
    dp=[0]*100005
    price = list(map(int, input().split()))
    pages = list(map(int, input().split()))
    for i in range(n):
        j=x
        while j>=price[i]:
            dp[j]=max(dp[j],dp[j-price[i]]+pages[i])
            j-=1
    return dp[x]
 
n,x = map(int,input().split())
print(BookShop(n,x))