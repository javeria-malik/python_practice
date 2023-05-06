#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maximum(x,y,z):
    return max(x,y,z)
maximum(9,100,89)


# In[2]:


def minimum(x,y,z):
    return min(x,y,z)
minimum(9,1000,90)


# In[4]:


"""Write a Python function to sum all the numbers in a list."""
    def sum_list(numbers):
        return sum(numbers)
    sum_list((9,0,7,6,5))


# In[9]:


"""Write a Python function to multiply all the numbers in a list."""
def multiply(numbers):
    product=1
    for x in numbers:
        product*=x
    return product
multiply((6,8,9))


# In[13]:


def products(alpha):
    product=1
    for x in alpha:
        product*=x
    return product
products((0,8,766))


# In[28]:


"""Write a Python program to reverse a string. """
def reverse_str(str):
    new=str.split()
    new.reverse()
    return " ".join(new)
reverse_str("j s j bb sjhab")


# In[24]:


x="j i y a"
y=x.split()
y.reverse()
print(y)
" ".join(y)


# In[37]:


def reverse_function(str):
    #str[::-1]
    return str[::2]
reverse_function("javeria")


# In[39]:


"""Write a Python function to calculate the factorial of a number (a non-negative integer)
. The function accepts the number as an argumen"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(9)
factorial(0)


# In[42]:


"""Write a Python function to check whether a number falls within a given range."""
def presence(num,x,y):
    if x<=num and y>=num:
        return True
    else:
        return "sorry"
presence(7,89,99)
presence(100,90,110)


# In[47]:


"""Write a Python function that accepts a string and counts the number of upper and lower case letters."""
def count(str):
uppercase = 0
lowercase = 0
for x in str:
    if x.isupper():
        uppercase+=1
    elif x.islower():
        lowercase+=1
return(uppercase,lowercase)
count("hello JIYa")


# In[48]:


def count(string):
    uppercase = 0
    lowercase = 0
    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    return (uppercase, lowercase)

count("hello JIYa")


# In[55]:


"""Write a Python function that takes a list and returns a new list with distinct elements from the first list"""
def distinct_list(lst):
    return list(set(lst))
distinct_list([1,2,3,3,3,3,4,5])


# In[58]:


"""Write a Python function that takes a number as a parameter and checks whether the number is prime or not"""
def isprime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
isprime(9)
isprime(2)


# In[61]:


def is_prime(num):
    """
    Returns True if the given number is prime, False otherwise.
    """
    #if num < 2:
      #  return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for num in range(2, 31):
    if is_prime(num):
        print(num, end=' ')
isprime(90)


# In[67]:


"""Write a Python program to print the even numbers from a given list."""
def iseven(list):
    even=[]
    for x in list:
        if x%2==0:
            print(x,end=" ")
iseven([2,4,9,8,6,5,44,65,56])


# In[68]:


"""Write a Python function that checks whether a passed string is a palindrome or not"""
def ispalindrome(str):
    return str== str[::-1]
ispalindrome("madam")


# In[69]:


import time

def greet(name):
    """
    Greets the given name.
    """
    print(f"Hello, {name}!")

def delayed_greeting(name, delay):
    """
    Invokes the greet function after a specified delay.
    """
    time.sleep(delay)
    greet(name)

# Call the delayed_greeting function with a delay of 5 seconds
delayed_greeting("John", 15)


# In[ ]:




