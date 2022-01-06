# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# generate random integer values
from random import seed
from random import randint


def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def setLCM(bound):
    lcm = 1
    for i in range(1,bound + 1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def rSqModularExponentiation(b,k,n):
    # computes b^k mod n, with b<n
    a = 1
    if k == 0:
        return a
    bin_k_str = bin(k)[2:][::-1]  # get bit representation
    t = len(bin_k_str)
    c = b
    if bin_k_str[0] == '1':
        a = b
    for i in range(1, t):
        c = c ** 2 % n
        if bin_k_str[i] == '1':
            a = c * a % n
    return a


def Pollard_P_minus_1(n, B):
    """
        Input: an odd composite number n, and a bound B.
        Output: a non-trivial factor d of n.
    """
    maxRepetitions = 9000
    triedAs = []
    k = setLCM(B)
    while maxRepetitions > 0:
        a = randint(2, n-2)
        while a in triedAs and len(triedAs) < n-3:
            a = randint(2, n-2)
        triedAs.append(a)
        a = rSqModularExponentiation(a,k,n)
        d = gcd(a-1,n)
        if d == 1 or d == n:
            maxRepetitions -= 1
        else:
            return d
    print("FAILURE")
    return None


if __name__ == '__main__':
    _B = 13  # bound
    the_n = 101 * 93 * 79  # int(input("n = "))  # number to factor

    if the_n % 2 == 0:
        print("No bueno")
        exit(1)

    possibleB = input("B = ").strip()
    if len(possibleB) > 0 and possibleB.isnumeric():
        _B = int(possibleB)

    # seed random number generator
    seed(1)
    x = Pollard_P_minus_1(the_n,_B)
    print(the_n // x)
    # print("The factor is:", Pollard_P_minus_1(the_n,_B))

