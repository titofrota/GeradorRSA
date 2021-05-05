def xor(data: bytes, mask: bytes):
    return bytes([_a ^ _b for _a,_b in zip(data, mask)])

if __name__ == "__main__":
    print(xor(b'Oi Italo', b'Tchau Italo'))