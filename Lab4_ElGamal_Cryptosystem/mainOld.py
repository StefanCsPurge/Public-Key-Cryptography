import random

private_key = (0, 0, 0)
public_key = 0


def fast_exponentiation(g, a, p, m=-1):
    result = 1
    while a:
        if a % 2 == 1:
            result = (result * g) % p
        g = (g * g) % p
        a //= 2

    if m != -1:
        result = (m * result) % p
    return result


def isPrime(x):
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def generate_large_random_prime():
    lower_bound = 434243
    upper_bound = 24324234
    starting_point = random.randint(lower_bound, upper_bound)
    potential_prime = starting_point * 2 + 1
    while not isPrime(potential_prime):
        potential_prime += 2
    return potential_prime


def find_generator(p):
    for potential_generator in range(2, p):
        visited = {}
        group_member = 1
        found_generator = True
        for _ in range(1, p):
            group_member = (group_member * potential_generator) % p
            try:
                if visited[group_member] == 1:
                    found_generator = False
            except:
                visited[group_member] = 1
        if found_generator:
            return potential_generator
    raise ArithmeticError("p is not prime")


def generate_private_key(p):
    return random.randint(1, p - 2)


def generate_keys():
    p = generate_large_random_prime()
    g = find_generator(p)
    a = generate_private_key(p)
    gap = fast_exponentiation(g, a, p)   # g^a mod p
    return (p, g, gap), a


def encrypt(m, public_key):
    #  public_key is (p, g, g^a)
    k = generate_private_key(public_key[0])
    alpha = fast_exponentiation(public_key[1], k, public_key[0])
    beta = fast_exponentiation(public_key[2], k, public_key[0], m)
    return (alpha, beta)


def decrypt(c, private_key, p):
    #  c is (alpha, beta)
    return fast_exponentiation(c[0], p-1-private_key, p, c[1])


if __name__ == '__main__':

    ## Key generation
    print("\nGenerated keys:")
    public_key, private_key = generate_keys()
    print(public_key)
    print(private_key)
    
    ## Encryption
    print("\nBobby encrypts his dank message:")
    m = 420    # message,  0 < m < p-1
    c = encrypt(m, public_key)  # cyphertext
    print(c)

    ## Decryption
    print("\nAlice get the dank message in the Wonderland and decrypts it:")
    plaintext = decrypt(c, private_key, public_key[0])
    print(plaintext)
    print("\nblaze it\n")