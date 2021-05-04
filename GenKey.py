import random 
import math
from ExtendedEuclideanAlgorithm import gcdExtended
from GeneratePrime import bitLength

def genKey(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(1, phi - 1)
        if math.gcd(e, phi) == 1: 
            u, s, t = gcdExtended(phi, e)
            if u == (s * phi + t * e):
                d = t % phi
                break
    
    
    publicKey = (e, n)
    privateKey = d
    return publicKey, privateKey


def main(): 
    p = bitLength(1024)
    q = bitLength(1024)
    publicKey, privateKey = genKey(p, q)
    print(publicKey)
    print(privateKey)
    

if __name__ == "__main__":
    main()
    
    
    