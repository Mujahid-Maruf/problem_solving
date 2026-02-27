L, R = map(int, input().split())

def fibonacciBetween(l, r):
    if r < 0:
        return []
        
    a, b = 0, 1
    result = set() 

    while a <= r:
        if a >= l:
            result.add(a)
        a, b = b, a + b

    return sorted(list(result))

finalResult = fibonacciBetween(L, R)

for i in finalResult:
    print(i)