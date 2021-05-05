from binascii import hexlify

def xor(data: bytes, mask: bytes):
    return bytes([_a ^ _b for _a,_b in zip(data, mask)])

if __name__ == "__main__":
    print(hexlify(xor(b'11', b'10')))