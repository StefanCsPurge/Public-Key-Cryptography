##############################################################
# The Extended Euclidean Algorithm

def EEA(a,b):
    # output: d=(a,b) and u, v (integers) s.t. a*u + b*v = d
    saved_a = a
    saved_b = b
    u2 = 1
    u1 = 0
    v2 = 0
    v1 = 1
    while b > 0:
        q = a // b
        r = a - q * b
        u = u2 - q * u1
        v = v2 - q * v1
        a = b
        b = r
        u2 = u1
        u1 = u
        v2 = v1
        v1 = v
    d = a
    u = u2
    v = v2
    print("\n{} = {} * {} + {} * {}".format(d,saved_a,u,saved_b,v))
    if u < 0:
        u = saved_b + u
    return u


if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b (mod) = "))
    print("{}^-1 mod {} = {}".format(a,b,EEA(a,b)))
    
