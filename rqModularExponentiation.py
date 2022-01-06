# Repeaded Squaring Modular Exponentiation
import time

max_steps = 420

while max_steps > 0:
    print("\nThis will compute b^k mod n, with b<n")
    b = int(input("b = "))
    k = int(input("k = "))
    n = int(input("n = "))

    a = 1
    if k == 0:
        print(a)
        exit(0)

    bin_k_str = bin(k)[2:][::-1] # get bit representation
    t = len(bin_k_str)
    # print(t)

    c = b
    if bin_k_str[0] == '1':
        a = b

    for i in range(1,t):
        c = c**2 % n
        if bin_k_str[i] == '1':
            a = c * a % n

    print("{}^{} mod {} = {} or {}\n".format(b,k,n,a,a-n))

    try:
        input("Press Enter to continue...")
    except:
        pass
    max_steps -= 1

print("Too many computations today lad, take it easy.")
