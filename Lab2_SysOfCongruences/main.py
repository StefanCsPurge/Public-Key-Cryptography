# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
4. Algorithm for solving systems of congruences.
   Using Chinese Remainder Theorem, to solve systems of the form:
   | x = a_1 (mod n_1)
   | x = a_2 (mod n_2)
   | . . . . . . . .
   | x = a_r (mod n_r)
"""


class CongruencesSystemSolver:
    def __init__(self, systemInputFile):
        self.__sysFile = systemInputFile
        self.N = 1
        self.modulos = []
        self.r = 0
        self.a = []
        self.readSystem()
        self.x = None

    def readSystem(self):
        file = open(self.__sysFile, "r")
        n_gcd = 1
        for line in file:
            if len(line.strip()) < 2:
                continue
            a_n = line.strip().split('=')[1].strip().split('mod')
            self.a.append(int(a_n[0].strip()))
            self.modulos.append(int(a_n[1].strip()))
            n_gcd = self.gcd(n_gcd,self.modulos[-1])
            if n_gcd != 1:
                print("Modulos are not relatively prime!")
                self.r = 0
                break
            self.N *= self.modulos[-1]
            self.r += 1
        file.close()

    @staticmethod
    def gcd(a,b):
        while b:
            r = a % b
            a = b
            b = r
        return a

    @staticmethod
    # The Extended Euclidean Algorithm
    def EEA(a,b):
        # compute a^-1 mod b
        # d=(a,b) and u, v (integers) s.t. a*u + b*v = d
        if CongruencesSystemSolver.gcd(a,b) != 1:
            print("No solution for {}^-1 mod {}".format(a,b))
            return None
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
        u = u2
        if u < 0:
            u = saved_b + u
        return u

    def solveSystem(self):
        if self.r > 0:
            self.x = 0
        for i in range(self.r):
            N_i = self.N // self.modulos[i]
            K_i = self.EEA(N_i, self.modulos[i])
            if K_i is None:
                return None
            self.x += self.a[i] * N_i * K_i
            self.x %= self.N
        return self.x


if __name__ == '__main__':
    my_system = CongruencesSystemSolver("system.in")
    x = my_system.solveSystem()
    print("The solution is:",x)


