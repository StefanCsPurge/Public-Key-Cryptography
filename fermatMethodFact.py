# Fermat's method factorization
import math 

n = 200819
t0 = int(math.sqrt(n))
print(t0)

for i in range(1,21):
    t = t0 + i
    res = t * t - n
    root = math.sqrt(res)
    if int(root + 0.5) ** 2 == res:
        s = int(root)
        print("Step {} , {} is a perfect square".format(i,res))
        print("s={}, t={}, {} = {} * {}".format(s,t,n,t-s,t+s))
        break
    else:
        print("Step {} , {} not a perfect square".format(i,res)) 

