#!/usr/bin/env python
# coding: utf-8

# # ceaser cipher

# #code

# In[37]:


def encrypt(W):        #Function for encrypting thw given word into ceasesr cipher
    for i in W:
        if ord(i)<88:
            print(chr(ord(i)+3),end='')
        elif i=='X':
            print('A',end='')
        elif i=='Y':
            print('B',end='')
        elif i=='Z':
            print('C',end='')
            
            
def decrypt(w):        #Function for decrypting the cypher text
    for i in w:
        if ord(i)>67:
            print(chr(ord(i)-3),end='')
        elif i=='C':
            print('Z',end='')
        elif i=='B':
            print('Y',end='')
        elif i=='A':
            print('X',end='')
    
    
    


# # Vegenere cipher 

# #code

# In[1]:


def vencrypt(plain_text,key):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code=[]
    count=0
    for i in plain_text:
        for j in key:
            code.append(j)
            count += 1
            if count ==len(plain_text):
                break
        if count ==len(plain_text):
            break
    code = ''.join(code)
    
    for i in  range (0,len(plain_text)):
        x=code[i]
        y=plain_text[i]
        f=alpha.index(x)+alpha.index(y)
        if f>=26:
            f = f-26
        print(alpha[f],end='')
        
def vdecrypt(cipher_text,key):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code=[]
    count=0
    for i in cipher_text:
        for j in key:
            code.append(j)
            count += 1
            if count ==len(cipher_text):
                break
        if count ==len(cipher_text):
            break
    code = ''.join(code)
    
    for i in  range (0,len(cipher_text)):
        x=code[i]
        y=cipher_text[i]
        f=alpha.index(y)-alpha.index(x)
        print(alpha[f],end='')
        
    

