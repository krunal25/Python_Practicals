#!/usr/bin/env python
# coding: utf-8

# In[89]:


# Find max no
def mymax(list1):
    maxval = 0
    for i in range(0, len(list1)):
        if(list1[i] > maxval):
            maxval = list1[i]
    return maxval

mymax([77,48,19,17,93,90])


# In[90]:


# Find max no
def mymax1(list2):
    maxval1 = list2[0]
    for j in list2:
        if maxval1 < j:
            maxval1 = j
    return maxval1

mymax1([77,48,19,17,93,90])


# In[6]:


# Find max no
list2 = [77,48,19,17,93,90]
def mymax3(list2):
    return sorted(list2)[-1]
mymax3(list2)


# In[92]:


# Find min no
list3 = [77,48,19,17,93,90]
def mymin(list3):
    return sorted(list3)[0]
mymin(list3)


# In[85]:


# Aversge
avgl= [10,15,20,25,30,7]
avg = (avgl[0] + avgl[1] +avgl[2]+avgl[3]+avgl[4]+avgl[5]) / len(avgl)
avg


# In[1]:


# Aversge
avgl2= [10,15,20,25,30,7]
avg2 = sum(avgl2) / len(avgl2)
avg2


# In[94]:


x = int(input("Ebt"))


# In[23]:


def minimum(list7):
    minval7 = max(list7) 
    for x in list7: 
        if x < max(list7):
            minval7 = x 
            return x

minimum([611,2,3,0,66]) 


# In[13]:


# Calculate Distance
import math

x = int(input(" Enter x :"))
x1 = int(input(" Enter x1 :"))

y = int(input(" Enter y :"))
y1 = int(input(" Enter y1 :"))

dis = math.sqrt((x-x1)**2 + (y-y1)**2 )
dis


# In[20]:


# Calculate Distance
import math
def mydistance(list7):
    
    x = int(input(" Enter x :"))
    x1 = int(input(" Enter x1 :"))
    y = int(input(" Enter y :"))
    y1 = int(input(" Enter y1 :"))
    dis = math.sqrt((x-x1)**2 + (y-y1)**2 )
    print(dis)
mydistance(dis) 


# In[ ]:





# In[ ]:




