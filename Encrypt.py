from PaddingScheme import oaep_encode
from GenKey import genKey, bitLength
from binascii import hexlify
from Convert import os2ip, i2osp
import string 

def encrypt(message: string, e: int, n: int):
    # Converter Message em plain text com o padding scheme 
    x, y, m = oaep_encode(message, 1024, 32, 16)  
    c = pow(os2ip(m), e, n)
    return i2osp(c, 1024)  

def decrypt(cypherText: string, d: int, n: int):
    c = os2ip(cypherText)
    m = pow(c, d, n)
     
    
if __name__ == "__main__":
    p = bitLength(1024)
    q = bitLength(1024)
    publicKey, privateKey = genKey(p, q)
    c = encrypt("Oi Italo", publicKey[0], publicKey[1])  