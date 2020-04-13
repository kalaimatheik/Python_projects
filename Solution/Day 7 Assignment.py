#!/usr/bin/env python
# coding: utf-8

# # Question 1: Sum of digits in a given number

# In[ ]:


def getSum(n):   
    sum = 0    
    while(n > 0): 
        sum += int(n%10) 
        n = int(n/10)    
  
    return sum
  
n=int(input("Enter the digit: "))
x=getSum(n)

if len(str(x))>1:
    y=getSum(x)
    print("Sum of digit: ",y)
else:
      print("Sum of digit: ", x)


# # Question 2: NOTEBOOK ON MAP,LAMBDA,FILTER,REDUCE

# In[ ]:


#MAPS():

#SYNTAX: map(funtion, iterables)
#-usual:

def sqr(a):
    return a*a

x=sqr(5)
print(x)

#With map 
def sqr(a):
    return a*a

x=map(sqr,[2,5,6])
print(x)#type map- convert it into list, tuple
print(list(x))



def sqr(a,b):
    return a-b

x=map(sqr,[2,5,6],[1,2,3])
print(x)#type map- convert it into list, tuple
print(list(x))


# In[ ]:


# LAMBDA:

#no name, lamda attribute: expression
#code short, fast, in single line
#when not goint to be used or many times-- it is effiecint
#no name associated with it
#for example 1000s of of lines r tehre and only one time the function is going to be exeuted.

#sytax: lambda arugment:expression

#wthout lambda
def sqr(a):
    return a*a

x=sqr(5)
print(x)

#With lambda:

xx=lambda a:a*a
print(xx(5))

def prq(q):
    return lambda p:p+q

x=prq(1)
print(x)
print(type(x))
print(x(2))


# In[ ]:


#Quadratic:

z= lambda x,y:5*x+3*y
print(z(1,2))

p= lambda x,y:(x+y)**2
print(p(1,2))


# In[ ]:


#using lamda inside map()
l=[1,2,3,4]
print(list(map(lambda x:x+3,l)))

#print(list(x))


# In[ ]:


#Filter:

#Syntax: filter(funtion,iterables)

def func(a):
    if a>=3:
        return a
    
print(list(map(func,[1,2,3,4,5,6])))
print(list(filter(func,[1,2,3,4,5,6])))

print(list(map(lambda x:x>=3,[1,2,3,4,5,6])))
print(list(filter(lambda x:x>=3,[1,2,3,4,5,6])))


# In[ ]:


#Reduce:- gives a single value#
#for cumilative oepration  such  as additon of elements in the list
#Syntax reduce(funtion,iterables)
#should import it from functools

#import functools
from functools import reduce

def sqr(a,b):
    return a+b

print(reduce(sqr,[1,2,3,4]))
#the list is passed to b and a will be 0
#no converstion to list is needed as it returns only 1 value

#add a=0
print(reduce(lambda a,b:a+b,[1,2,3,4]))

#multi a=1
print(reduce(lambda a,b:a*b,[1,2,3,4]))


# In[ ]:


#filter witin map

#python from inner to outer

print(list(map(lambda x:x+x,filter(lambda x:x>=3,[1,2,3,4,5,6]))))


# In[ ]:


#map within filter

print(list(filter(lambda x:x>3,map(lambda x:x+3,[1,2,3,4,5,6]))))


# In[ ]:


#map and filter within reduce

print(reduce (lambda x,y:x+y, map(lambda x:x+x, filter(lambda x:x>=3,[1,2,3,4,5,6]))))

