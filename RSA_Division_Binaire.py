import numpy as np
print("==========================================================================================")
def noise(vect_msg):

### on fait une copie du vecteur initial
    vect = vect_msg.copy()
### une chance sur quatre de ne pas bruitéer le vecteur
    test = np.random.randint(0,4)
    if test>0:
        index = np.random.randint(0,np.size(vect))
        vect[index] = (vect[index] +1)%2
    return vect
vecteur = [
    [0,0,0,0,0,0,0],
    [1,1,0,1,0,0,1],
    [0,1,0,1,0,1,0],
    [1,0,0,0,0,1,1],
    [1,0,0,1,1,0,0],
    [0,1,0,0,1,0,1],
    [1,1,0,0,1,1,0],
    [0,0,0,1,1,1,1],
    [1,1,1,0,0,0,0],
    [0,0,1,1,0,0,1],
    [1,0,1,1,0,1,0],
    [0,1,1,0,0,1,1],
    [0,1,1,1,1,0,0],
    [1,0,1,0,1,0,1],
    [0,0,1,0,1,1,0],
    [1,1,1,1,1,1,1]

]

Matrice = np.array([
    [1,1,0,1],
    [1,0,1,1],
    [1,0,0,0],
    [0,1,1,1],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
])

    

msg= input('veuillez choisir un mot pour tester le pogramme:')
message=''
msg = [str(ord(j)) for j in msg]
print("message =",msg)
for i, k in enumerate (msg):
    if len(k) < 3:
        while len(k) < 3:
            k = '0' + k
        msg[i] = k
for j in range(len(msg)):
    message = message + str(msg[j])
               
while len(message) %4 != 0:
    message =message +'0'

message2=[]
a = 4
b = 0
tabi = []
for i in range(int(len(message)/4)):#on l'intergre dans la liste
    message2.append(message[b:a])
    a = a+4
    b = a-4
    
print("message diviser en 4 partie",message2)
for i in range(len(message2)):
        
    messagebin = str(bin(int(message2[i])))[2:]
    while True:
        if len(messagebin)%4!=0:
            messagebin='0'+messagebin
        else:
            break
    while True:
        if len(messagebin)!=16:
            messagebin='0'+'0'+'0'+'0'+messagebin
        if len(messagebin)==16:
            break
    a=4
    b=a-4
    for i in range(int(len(messagebin)/4)):
        tabi.append(messagebin[b:a])
        a=a+4
        b=b+4
print("tableau bianire en 4",tabi)
print("==========================================================================================")



tableau = []
for x in range(len(tabi)):
    matr = [[],[],[],[]]
    Bit = tabi[x]
    for i in range(0,4):
        matr[i] = int(Bit[i])
    prod = (Matrice@matr)
    #prod = str(prod)

    for i,v in enumerate(prod):

        prod[i] = v%2



    bruité = noise(prod)

    v = []
    for j in vecteur: 
        add = []
        for i in range(0,7):
            add.append((bruité[i] + (j[i])%2))

        d = 0

        for i in add:
            if i == 1:
                d +=1
        if d == 0 or d ==1:
            v = j
            break
    Donner=str(v[2])+str(v[4])+str(v[5])+str(v[6])
    tableau.append(Donner)
chainecara =''

a=16
b=a-16
for i in range (len(msg)):
    chainecara = chainecara+msg[i]

a=3
b=a-3
c=''
decriptionfinal=''
lenphrase=int(len(chainecara)/3)
for i in range(lenphrase):
    
    
    c=chainecara[b:a]
        
    decriptionfinal = decriptionfinal + chr(int(c))
    a=a+3
    b=a-3
print(decriptionfinal)
