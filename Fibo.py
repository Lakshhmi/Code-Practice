
# coding: utf-8

# In[6]:

#Fibonocci Number Module
def fibo(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        c=a+b
        a=b
        b=c        
def fibo2(n):
    result = []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result       
    
    

