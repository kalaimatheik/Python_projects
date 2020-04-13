#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1:Creating a dictionary

def abc(n):
    i=1
    dict1={}
    while i<=n:
        
        dict1.update({i:i*i})
        i+=1
    return dict1     
        
        
dict1=abc(3)
print(dict1)


# In[1]:


#Question 2:Creating list

def abc(b):
    lst=[]    
    for i in range(1,b+1):
        lst.append(i)
    return lst

def xyz():
    lst1=abc(50)
    print(lst1)
    a,b=input("Enter input for start and end index").split()
    for i in range(int(a),(int(b)+1)):
        print(lst1[i])
    
    
xyz()



    


# In[2]:


#list

lst=list(range(1,51))
print(lst)


# In[7]:


#multiple assignemnt:

cat=["acat",'bcat','ccat']
a=cat[0]
b=cat[1]
c=cat[2]

print (a,b,c)

cat=["acat",'bcat','ccat']
x,y,z=cat
print(x,y,z)

p,q,r=1,11,3
print(p,q,r)
#swap

u=1
v=2
u,v=v,u

print(u,v)


# In[ ]:





# In[8]:


#LIST:
cat=["acat",'bcat','ccat']
print(cat.index("bcat"))


# In[ ]:




