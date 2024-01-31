import random
print("-----------------------------------------")
def list_prem(n):
    #crétion d'une liste contenant tous les nombres premiers de 2 a n
    tab=[2]
    i=3
    y=0
    estprem= True
    while i < n:
        if  i%2 != 0:
            for y in tab:
                if i%y==0:
                    estprem= False
        else:
            estprem = False
        if estprem== True:
            tab.append(i)
        estprem = True
        i +=1
    return tab

def extended_pgcd(a, b):
    #calcul de l'extension du pgcd
    d, u, v = a, 1, 0
    d2, u2, v2 = b, 0, 1
    
    while d2 != 0:
        q = d//d2
        d3, u3, v3 = d, u, v
        d, u, v = d2, u2, v2
        d2 = d3 - q*d2 
        u2 = u3 - q*u2 
        v2 = v3 - q*v2
    return (d, u, v) 

def key_creation():
    #création des clés publiques et privées
    p = 0
    q = 0
    liste=list_prem(1000)
    while p==q:
        p,q = random.randint(0,len(liste)-1),random.randint(0,len(liste)-1)
        p,q = liste[p], liste[q]

    #calcul n et phi(n)
    n= p*q
    phi = (p -1) * (q - 1)

    #créé les clé publique grace au pgcd
    e = 2
    while True:
        d,_,_=extended_pgcd(e,phi)
        if d== 1:
            break
        else:
            e +=1
    pub = (e)
    
    #créé les clé priver grace a la cle publique et le modulo de phi

    i = 2
    
    while True:
        g = (e * i) % phi
        if g == 1:
            break
        else:
            i +=1
    priv = (i)
    print("p:",p,"q:",q,"n:",n,"pub:",pub,"priv:",priv)
    return n, priv, pub

def convert(msg):
#transforme le message en chiffre 

    message=''
    msg = [str(ord(j)) for j in msg]
    print("message=",msg)
    for i, k in enumerate (msg):
        if len(k) < 3:
            while len(k) < 3:
                k = '0' + k
            msg[i] = k
    for j in range(len(msg)):
        message = message + str(msg[j])

#met le message en ascii en paquet de 4 du message et rajoute des zero dans les paquet qui ne sont pas egal a 4  
    message2=[]
   
    test= '4'
    while len(message) %4 != 0:
        message =message +'0'
    a = 4
    b = 0
    for i in range(int(len(message)/4)):
        message2.append(message[b:a])
        a = a+4
        b = a-4

    return message2

def encryption(n,pub,msg):

    message2 = convert(msg)#intergre la fonction convert dans encription
    #pour chaque valeur du tableau créé le mewssage cripter grace a la formule {m**pub |mod n|}
    for i in range(len(message2)):
        message2[i] = str(pow(int(message2[i]),pub,n))
    return message2


def decryption(n,priv,msg):
    #pour chaque valeur du tableau transfome le mewssage cripter et le decripte grace a la formule {m2**priv |mod n|}

    for i in range(len(msg)):
        msg[i] = str(pow(int(msg[i]),priv,n))
    print("msg après decription",msg)

    for i in range(len(msg)):
        while len(msg[i]) % 4 != 0:
            msg[i] = '0' + msg[i]
    chcara = ''
    #prnd chaque valeur du tableau et créé un grand chiffre 
    for i in range(len(msg)):
        chcara = chcara + msg[i]
    print("ici j'ai une longe chaine de caractère",chcara)
    
    #prennd le grand chiffre et trouve chaque caractere
    a=3
    b=a-3
    c=''
    decriptionfinal=''
    lenphrase=int(len(chcara)/3)
    for i in range(lenphrase):
    
    
        c=chcara[b:a]
        
        decriptionfinal = decriptionfinal + chr(int(c))
        a=a+3
        b=a-3
   
    
    return decriptionfinal

n,priv,pub = key_creation()
for i in range(1):
    msg = input("le mot: ") 
    msgi=encryption(n,pub,msg)
    print("message cripté=",msgi)
    print("message décripté",decryption(n,priv,msgi))
    