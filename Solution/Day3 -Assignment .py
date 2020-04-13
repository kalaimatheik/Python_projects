#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1:
 
#Grades: A,B,C,D,E,FAIL

marks=int(input("Enter the Marks:"))
#print(marks)

if marks>=90:
    print("Grade is A")
    
elif marks>=80 and marks<90:
    print("Grade is B")
    
elif marks>=70 and marks<80:
    print("Grade is c")

elif marks>=60 and marks<70:
    print("Grade is D")
    
elif marks>=50 and marks<60:
    print("Grade is E")
    
else:
    print("FAIL")


# In[6]:


#Question 2:

# Cricket Score:
import random

Guess_Score=int(input("Enter your Score:"))
#print("The score guessed",Guess_Score)
Score=random.randrange(1,250)
print("Score generated:",Score)
Diff=abs(Score-Guess_Score)
print("Difference:",Diff)

if Guess_Score>=1 and Guess_Score<=250:
    if Diff<=10 :
        print("Close by you are true Indian Fan")
    else:
        print("You dont watch much")   
    
else:
    print("Reduce your expectation for 20-20 cricket")

