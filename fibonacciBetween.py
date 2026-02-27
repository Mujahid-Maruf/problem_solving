L, R = map(int, input().split())

def fibonacciBetween(l,r,n):
    series = [0, 1]
    for i in range(2, n):
        if series[-1]+series[-2] <=r :
            series.append(series[-1] + series[-2])
    return series[:n]

initResult=fibonacciBetween(R,R)
intermidiateResult=set(initResult)
a=list(intermidiateResult)
a.sort()

for i in a:
    print(i)