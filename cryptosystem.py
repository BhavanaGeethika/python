def isprime(n):
    i = 2         
    count = 0        
    while i < n:             
        if n % i == 0:
            count += 1
        i += 1
    if count == 0:
        return True
    else:
        return False
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x   
def cryptosystem(b):
    mode = input("encrypt or decrypt:")
    prime = []
    from random import choice
    for i in range(1,1000):
        if isprime(i):
            prime.append(i)
    p = choice(prime)
    prime.remove(p)
    q = choice(prime)
    prime.remove(q)
    n = p*q
    exponent = [] 
    for pue in range(3,n):
        if pue % 2 != 0:
            if gcd(pue,p-1) == 1 and gcd(pue,q-1) == 1:
                exponent.append(pue)
    e = choice(exponent)
    f = (p-1) * (q-1) 
    c = pow(b,e,n)
    public_key = (n,e)
    #for d in range(0,f):
        #if (d*e == 1 % f):
            #b = pow(c,d,n)
            #break                
    if mode == "encrypt":
        return c
    elif mode == "decrypt":
        for d in range(0,f):
            if (d*e == 1 % f):
                b = pow(c,d,n)
                break          
        return b                     
def reverse(string):
    string = ''.join(reversed(string))
    return string
symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
ln = len(symbol)
s = input("enter any text message:")
l = list(s)
blockinteger = 0
for i in range(0,len(l)):
    k = symbol.index(l[i])
    blockinteger += k * (len(symbol)**i)    
encrypted = cryptosystem(blockinteger)
print(encrypted)
decrypted = cryptosystem(blockinteger)
print(decrypted)
m = ""
while i >= 0:
    d = decrypted // (len(symbol)**i)
    m += symbol[d]
    decrypted = decrypted % (len(symbol)**i)
    i = i - 1
print(reverse(m))
