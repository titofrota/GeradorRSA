def os2ip(x: bytes):
    return int.from_bytes(x, byteorder='big')

def i2osp(x: int, xlen: int):
    return x.to_bytes(xlen, byteorder='big')
    
    