#!/usr/bin/env python
# coding: utf-8

# # Say "Hello, World!" With Python

# In[ ]:


my_string = "Hello, World!"
print(my_string)


# # Python If-Else

# In[1]:


n = int(input())
if (n%2!=0) or ((n%2==0) and n>= 6 and n<= 20):
    print('Weird')
else:
    print('Not Weird')


# # Arithmetic Operators

# In[4]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# # Python: Division

# In[7]:


from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# # Loops

# In[9]:


if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i) 


# # Write a function

# In[12]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4==0 and year%100!=0) or year%400 ==0:
        leap = True
    
    return leap
year = int(input())
print(is_leap(year))


# # Print Function

# In[13]:


from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    for x in range(1,n+1):
        print(x, sep='', end='')


# # List Comprehensions

# In[15]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if(i+j+k!=n)])


# # Find the Runner-Up Score!
# Eseguito con raw_input() su Python 2

# In[19]:


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    massimo=max(arr)
    runner_up=-101
    for i in range(n):
        if arr[i]!=massimo and arr[i]> runner_up:
            runner_up=arr[i]
    print(runner_up)


# # Nested Lists

# In[23]:


lista_studenti = []
lista_voti = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista_studenti.append([name,score])
    lista_voti.append(score)
s1 = sorted(set(lista_voti))[1]
for n,s in sorted(lista_studenti):
    if s==s1:
        print(n)


# # Finding the percentage

# In[2]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    lista_voti = list(student_marks[query_name])
    num_voti = len(lista_voti)
    somma_voti = sum(lista_voti)
    media = somma_voti/num_voti
    print('%.2f'%(media))


# # sWAP cASE

# In[4]:


def swap_case(s):
    stringa = ""
    for i in s:
        if i.islower():
            stringa += i.upper()
        elif i.isupper():
            stringa += i.lower()
        else:
            stringa += i
    return stringa

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# # String Split and Join

# In[6]:


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line= "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# # What's Your Name?

# In[8]:


def print_full_name(a, b):
    print("Hello " +a +" "+b+"! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# # Mutations

# In[10]:


def mutate_string(string, position, character):
    string = string[:(position)] + character + string[(position+1):]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# # Find a string

# In[12]:


def count_substring(string, sub_string):
    occorrenze = 0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            occorrenze+=1
    return occorrenze
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# # String Validators

# In[20]:


if __name__ == '__main__':
    s = input()
    print (any(i.isalnum() for i in s))
    print (any(i.isalpha() for i in s))
    print (any(i.isdigit() for i in s))
    print (any(i.islower() for i in s))
    print (any(i.isupper() for i in s))


# # Text Alignment
# Eseguito con raw_input() su Python 2

# In[22]:


#Replace all ______ with rjust, ljust or center. 

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)


# # Text Wrap

# In[26]:


import textwrap
def wrap(string, max_width):
    sub_string=textwrap.fill(string,max_width)
    return(sub_string)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# # Introduction to Sets

# In[29]:


from __future__ import division
def average(array):
    lista = []
    lista = set(array)
    av = sum(lista)/len(lista)
    return av
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print(result)


# # Set .add()

# In[30]:


N = int(input())
lista = []
for i in range(0,N):
    lista.append(input())
lista_distinct = set(lista)
num = len(lista_distinct)
print(num)


# # Calendar Module

# In[35]:


import calendar
data = input()
data_ddmmyyyy= data.split()
mm = int(data_ddmmyyyy[0])
dd = int(data_ddmmyyyy[1])
yyyy = int(data_ddmmyyyy[2])
giorno_settimana = calendar.weekday(yyyy, mm, dd)
if giorno_settimana == 0:
    print('MONDAY')
elif giorno_settimana == 1:
    print('TUESDAY')
elif giorno_settimana == 2:
    print('WEDNESDAY')
elif giorno_settimana == 3:
    print('THURSDAY')
elif giorno_settimana == 4:
    print('FRIDAY')
elif giorno_settimana == 5:
    print('SATURDAY')
else:
    print('SUNDAY')


# # Map and Lambda Function

# In[39]:


cube = lambda x: x*x*x 

def fibonacci(n):
    # return a list of fibonacci numbers
    lista = []
    for i in range(n):
        if i==0:
            lista.append(i)
        elif i ==1:
            lista.append(i)
        else:
            lista.append(lista[-1]+lista[-2])
    return(lista)

if __name__ == '__main__':
    n = int(input())
    fib = map(cube, fibonacci(n))
    print(fib)


# # Arrays

# In[40]:


import numpy
def arrays(arr):
    reverse_list = []
    for i in reversed(arr):
        reverse_list.append(i)
    reverse_array = numpy.array(reverse_list,float)
    return reverse_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# # Shape and Reshape

# In[41]:


import numpy
arr = input().split()
change_array = numpy.array(arr,dtype = int)
print(change_array.reshape((3, 3)))


# # Recursive Digit Sum

# In[1]:


import math
import os
import random
import re
import sys


def superDigit(n, k):
    somma = 0
    somma2 = 0
    for i in str(n):
        somma += int(i)
    somma *= k
    while somma >= 10:
        for i in str(somma):
            somma2 += int(i)
        somma = somma2
    return somma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)
    

    fptr.write(str(result) + '\n')

    fptr.close()


# # Viral Advertising

# In[2]:



import math
import os
import random
import re
import sys


def viralAdvertising(n):
    likes = 0
    people = 5
    for i in range(n):
        likes_per_day = people//2
        likes += likes_per_day
        people = likes_per_day * 3
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Birthday Cake Candles

# In[3]:



import math
import os
import random
import re
import sys
from collections import Counter 


def birthdayCakeCandles(candles):
    # Write your code here
    dizionario_presenti = {}
    lista_presenti = []
    lista = []
    for i in str(candles):
        lista_presenti.append(i)
    for i in lista_presenti:
        if i not in ('[',']',' ',','):
            lista.append(i)
    dizionario_presenti = Counter(lista)
    maximum = max(dizionario_presenti, key=dizionario_presenti.get)
    return dizionario_presenti[maximum]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:




