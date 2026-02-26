
lst=map(int,input().split())

for i in lst:
    if i%2==0:
        print(i,end=" ")
    else:
        print(-1,end=" ")

