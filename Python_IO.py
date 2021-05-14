#!/usr/bin/env python
# coding: utf-8

# # <span style="color:Green">Module</span>

# ***what are modules in python?**

# 1.**Modules refer to a file containinng python statement and sefinations.**<br>
# 2.**A file containing python code.for example calculater.py is called amodule.and its module name would be calculater.**<br>
# 3.**We use modulels  to break down large programs into small manageble and organized files.Furthermore,modules provide reusability of code.**<br>
# 4.**We can define our most use functions in a module and import it. insted of coping their defination into different programs**<br>
# 5.**Let us create a module .Type the following and save it as calculator.**
# 

# In[5]:


import calculator
calculator.sub(1,2)  # ok ? ha donew  ahi thi ne ?
# aa .ipynb file banave j colab and notebook j support kre aapde .py file joi a  # 


# In[7]:


import calculator as mc
mc.add(-2,-5)                 


# In[13]:


import calculator as mc
mc.sub(-5,-3) 


# In[14]:


print((-5)-(-3)) got it ?yes good


# In[5]:


from calculator import div,add
div(3,4)


# In[6]:


add(3,4)


# In[8]:


div(4,3)


# In[9]:


from calculator import *
div(3,4)


# In[10]:


add(3,4)


# In[11]:


sub(5,4)


# <span style="color:green">#import calculator as c</span>#alias<br>
# <span style="color:green">#from  calculator import add *import specific name</span><br>
# <span style="color:green">#from calculator import add, sub</span><br>
# <span style="color:green">#from calculator import *</span>#imported all the defination from the math module<br>

# # python module search path

# 1. while importing a module.python looks at several places. <br>
# A. Interpreter firts looks for a built-in module . <br>
# B. Then (if built-in module not found).python looks into a first of directories define in sys.path<br>
# C.The search is in this order.<br>
#    &nbsp; a. The current directory<br>
#    &nbsp; b.Pythonpath(an environment variable with a list of directories).The installation-dependent default directory.
# 

# __1.Python Files__<br>
# __2.Python object&class__

# ***Files***

# 1.file used to permantely store data in non-valtile memory(e.g.hard disk)<br>
# 2.When we want to read from or write to a file.we need to open it first.<br>
# 3.When we are done.it needs to be closed so that the resoureces that are tield with the file are freed.<br>
# 

# __A file operation takes place in the following order:__

# >>Open a file.<br>
# >>Read or write (perform operation).close the file.

# __*Opening files__

# Python has built in open()function open file.This function return a file object,also called a handle as it is usedx to read or modify the file accordingly.

# In[1]:


f = open('.\jjj.txt')
print(f.read())
#write kr hve jo kru  ha


# In[36]:


f = open('t5.txt','w')
fw = f.write("abcd")
print(fw)
f.close() 


# ***Mode Description***

# r:-Open a file for reading(default )<br>
# w:-Open a file for writing.create a new file if it does not exist or truncates the file if it exists.<br>
# x:-Opens a file for exclusive creation.If the file already exits,the operation files.<br>
# a:Opens file for appending at the and of the file without truncating it.creates a new File if it does not exist.<br>
# t:Opens in text mode(defalut)<br>
# b:Opens in binary modee.<br>
# t:opens a file for updating(reading and writing)

# In[9]:


f1 = open("file1.txt","w")
print(f1.write("This is line 1 \n"))
print(f1.write("This is line 2 \n"))
print(f1.write("This is line 3 \n"))
f1.close()
# Insert text using w mode


# In[10]:


f1 = open("file1.txt","a")
print(f1.write("this is append text"))
f1.close()
# add text using append mode


# In[13]:


f2 = open("file1.txt","r")
print(f2.read())
f2.close()
# read from file 


# In[14]:


f2 = open("file1.txt","r")
print(f2.readline())
f2.close()
# readline fun... read single line from starting of thr file 


# In[17]:


f2 = open("file1.txt","r")
print(f2.readline())
f2.tell()
# tell function show , at wthich our pointer is located 


# In[18]:


f2 = open("file1.txt","r")
print(f2.readlines())
f2.close()
# readlines fun... read whole file and " Return type : List "


# In[20]:


f2 = open("file1.txt","r")
print(f2.readline())
f2.seek(0)

# seek()  -   sets the file's current position at the offset


# In[24]:


list1 = ["krunal",1,'GVP',80.06]
f3 = open("list_to_file.txt","w")
for i in list1:
    f3.write(str(i) + " \n")
f3.close()    


# In[38]:


f5 = open("file5.txt","w")

print(f5.write("This is line 1 \n"))
print(f5.write("This is line 2 \n"))
print(f5.write("This is line 3 \n"))
print(f5.write("This is line 4 \n"))
print(f5.write("This is line 5 \n"))
print(f5.write("This is line 6 \n"))
print(f5.write("This is line 7 \n"))
print(f5.write("This is line 8 \n"))
print(f5.write("This is line 9 \n"))
print(f5.write("This is line 10 \n"))
print(f5.write("This is line 11 \n"))
print(f5.write("This is line 12 \n"))

print(f5.fileno())

f5.close()


# In[7]:


fdetach = open("fdetach.txt","w")
print(fdetach.write("one\ntwo\nthree\nfour\nfive"))
fdetach.detach()

#detach 


# In[14]:


f_fileno = open("f_fileno.txt","w")
print(f_fileno.write("one\ntwo\nthree\nfour\nfive"))
f_fileno.fileno()

#fileno 


# In[20]:


f = open("myflush.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

#flush


# In[21]:


f = open("myflush.txt", "r")

print(f.isatty())

#isatty


# In[22]:


f = open("myflush.txt", "r")

print(f.readable())

#isatty


# In[ ]:




