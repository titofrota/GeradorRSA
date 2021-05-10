from PaddingScheme import oaep_encode, oaep_decode, sha3_256
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

def sign(message: bytes, privateKey: int, n: int):
    messageHash = sha3_256(message)
    signature = pow(os2ip(messageHash), privateKey, n)
    return i2osp(signature, 1024)

def verify(message: bytes, signature: bytes, publicKey: int, n: int):
    messageHash = sha3_256(message)
    verifying = pow(os2ip(signature), publicKey, n)
    verifying = i2osp(verifying, 32)
    if verifying == messageHash:
        return True
    else :
        return False

    
if __name__ == "__main__":
    p = bitLength(1024)
    q = bitLength(1024)
    message = b"Teste messagem"
    messageTampered = b"Messagem corrompida"
    publicKey, privateKey = genKey(p, q)
    
    
    c, tamanhoMessage, TamanhoX, TamanhoY = encrypt("Tudo bem novo RSA", publicKey[0], publicKey[1])
    result = decrypt(c, privateKey, publicKey[1], tamanhoMessage, TamanhoX, TamanhoY)
    print(result)
    
    assinatura = sign(message, privateKey, publicKey[1])
    print(verify(message, assinatura, publicKey[0], publicKey[1]))

    