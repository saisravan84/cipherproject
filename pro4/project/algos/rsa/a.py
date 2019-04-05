#!C:\Users\sailakshmi01.trn.ITLINFOSYS\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html \n")
import cgi

form=cgi.FieldStorage()
plain_text=form.getvalue('name_pliantext')
key_1=int(form.getvalue('name_key1'))


def encrypt_char(m,e,n):
    c = m**e % n
    return c
def encrypt_string(s,a,b):
    e=a
    n=b
    q=s
    list1=list(q)
    list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'
           ,'w','x','y','z','?',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
           ,'Q','R','S','T','U','V','W','X','Y','Z','@','#','!','.','$','%','&','*','(',')','-','+']
    

    out=[]
    count=1
    for i in list1:
        for j in list2:
            if i==j:
                out.append(count)
                count=1
                break
            else:
                count=count+1
    
    final=[]
    for i in out:
        p=encrypt_char(i,e,n)
        
        if p<=66:
            final.append(list2[p-1])
        else:
            final.append(str(p))
    
    final2= ''.join(final)
    return final2

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

p=13

q=7

#print("prime numbers are:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
#print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
#print("[phi(n)]: " + str(phi) + "\n")


#print("Choose an e from a below coprimes array:\n")
#print(str(coprimes(phi)) + "\n")
e=int(key_1)
d=modinv(e,phi)
#print("\n encrypted keys are (e=" + str(e) + ", n=" + str(n) + ").\n")
#print("decrypted keys are (d=" + str(d) + ", n=" + str(n) + ").\n")

s = plain_text
#print("\nPlain message: " + s + "\n")
enc = encrypt_string(s,e,n)
#print("Encrypted message: " + enc + "\n")
print(enc)



