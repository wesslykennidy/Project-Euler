list_p = []
def sieveoferatosthenes(n):
    prime = [True]*(n+1)
    p = 2
    while (p*p <= n):
        if prime[p] == True:
            for i in range (p*p, n+1, p):
                prime[i] = False
        p += 1 
    
    for p in range (2,n+1):
        if prime[p]:
            list_p.append(p)
    return list_p

if __name__ == '__main__':
    n = 2000000
    result = sieveoferatosthenes(n)
    print (sum(result))
