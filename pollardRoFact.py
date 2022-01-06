# Pollards ro factorization
n = 9881
x0 = 2
x1 = None
x2 = None
d = 1
prev = [x0]
idx = 0

def f(x):
    return x * x + 1

def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def main():
    while d <= 1:
        x1 = f(x0) % n
        prev.append(x1)
        x2 = f(x1) % n
        prev.append(x2)
        idx += 2
        dif = abs(x2 - prev[idx//2])
        d = gcd(dif,n)
        print("x1 = {} , x2 = {} , (dif = {}) d = {}".format(x1,x2,dif,d))
        x0 = x2
        

    if d == n:
        print("Failure: d = n")
    else:
        print("{} = {} * {}".format(n,d,n/d))

 # main()

d = 3
while True:
    if gcd(d,3036) == 1:
        print(d)
        break
    d += 2
    
    
