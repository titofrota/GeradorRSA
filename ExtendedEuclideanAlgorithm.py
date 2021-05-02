def gcdExtended(a, b):
    assert a > b
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1 
        y0, y1 = y1, y0 - q * y1
    return b, y0, x0





# def main():
#     a, b = 35,15
#     g, x, y = gcdExtended(a, b) 
#     print("gcd(", a , "," , b, ") = ", g)

if __name__ == "__main__":
    print ( gcdExtended( 30, 5) )
    print ( gcdExtended( 17, 5) )
    print ( gcdExtended( 234232, 774) ) 
    