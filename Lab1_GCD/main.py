# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# def factor(n):
#     # decompose number in prime factors
#     factors = []  # list of (factor,power) pairs
#     nr = 0
#     while n % 2 == 0:
#         nr += 1
#         n //= 2
#     if nr > 0:
#         factors.append((2,nr))
#     d = 3
#     while d*d <= n:
#         nr = 0
#         while n % d == 0:
#             nr += 1
#             n //= d
#         if nr > 0:
#             factors.append((d,nr))
#         d += 2
#     if n != 1:
#         factors.append((n,1))
#     return factors

def remainder(nr, divisor):
    return nr - divisor * (nr // divisor)

#############################################################


# Euclid
# if h = base-10 number of digits of the smaller number,
# the complexity is O(h^2) - polynomial time algorithm
# or O(log^2 * n)
def gcd(a,b):
    while b:
        r = remainder(a,b)
        a = b
        b = r
    return a


# subtraction-based version
# less efficient
def gcd_subtractions(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

#############################################################


# linear O(n)
def gcd2(a,b):
    if a > b:
        r = a
        a = b
        b = r
    a2 = a
    while a:
        if remainder(b,a) == 0 and remainder(a2,a) == 0:
            return a
        a -= 1
    return b

#############################################################


# decomposition of numbers in prime factors
# not efficient at all
# Exponential time algorithm
def gcd3(a,b):
    div = 1
    d = 2
    while (d*d <= a or d*d <= b) and a > 1 and b > 1:
        while ((a/d).is_integer() or (b/d).is_integer()) and a > 1 and b > 1:
            if (a/d).is_integer() and (b/d).is_integer():
                div *= d
            if (a/d).is_integer():
                a //= d
            if (b/d).is_integer():
                b //= d
        if d == 2:
            d += 1
        else:
            d += 2

    if a == b or b == 0:
        div *= a
    elif a == 0:
        div = b
    return div


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
    print(f"\n{d} = {saved_a} * {u} + {saved_b} * {v}")
    return d,u,v


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_no = [(0,0),
               (0,99),
               (420,69),
               (1547,560),
               (2**100,600),
               (9520,560),
               (2**1000, 6004),
               (5**10,2**999),
               (2374,2112),
               (3832,210312),
               (999923,1231200)]

    for x,y in test_no:
        # EEA(x,y)
        # print(gcd_subtract(x,y))
        print(f"\n({x},{y})")
        start_time = time.process_time_ns()
        print(gcd(x,y))
        print("--- Euclid: time ---", time.process_time_ns() - start_time)

        start_time = time.process_time_ns()
        print(gcd2(x,y))
        print("--- Funny idea: time ---", time.process_time_ns() - start_time)

        start_time = time.process_time_ns()
        print(gcd3(x,y))
        print("--- Prime factors decomposition: time ---", time.process_time_ns() - start_time)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
