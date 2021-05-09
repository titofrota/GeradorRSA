from PaddingScheme import oaep_encode, oaep_decode
from GenKey import genKey, bitLength
from binascii import hexlify
from Convert import os2ip, i2osp
import string 

def encrypt(message: string, e: int, n: int):
    # Converter Message em plain text com o padding scheme 
    x, y, m = oaep_encode(message, 1024, 32, 16)
    
    print(x, y)
        
    c = pow(os2ip(m), e, n)
    return  c, len(m), len(x), len(y)

def decrypt(c: int, d: int, n: int, tamanhoDaMensagem: int, tamanhoX: int, tamanhoY: int):
    m = pow(c, d, n)

    messageBytes = i2osp(m, tamanhoDaMensagem)

    # TO DO utilzar o m no decode de oaep para mostrar o m inicial
    messageOaep = oaep_decode(messageBytes[:tamanhoX], messageBytes[tamanhoX:tamanhoX + tamanhoY])

    return messageOaep[1]
    
    
if __name__ == "__main__":
    p = bitLength(1024)
    q = bitLength(1024)
    publicKey, privateKey = genKey(p, q)
    c, tamanhoMessage, TamanhoX, TamanhoY = encrypt("Oi Italo", publicKey[0], publicKey[1])
    result = decrypt(c, privateKey, publicKey[1], tamanhoMessage, TamanhoX, TamanhoY)
    print(result)
    