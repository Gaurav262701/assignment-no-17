#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no 2
def check(a):
    regrex = eval(a)
    if regrex:
        return True
    else:
        return False
    
print(check("2<7<15"))
print(check("13>44>33>1"))
print(check("1<2<6<9>3"))


# In[2]:


#Answer no 3
def replacevowel(test_str,k):
    vowels = 'AEIOUaeiou'
    for ele in vowels:
        test_str = test_str.replace(ele,k)
    return test_str

input_str = "Ineuron is Best"
k = "#"
print("Given string:",input_str)
print("Given specified characters:",k)

print("After replacing vowels with thhe specified characters:",replacevowel(input_str,k))


# In[3]:


#Answer no 4
def recur_fac(n):
    if n == 1:
        return n
    else:
        return n*recur_fac(n-1)
num = 5
if num < 0:
    print("enter a positive number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("the factorial of",num,"is",recur_fac(num) )


# In[8]:


#Answer no 5
string1 = abcbba
string2 = abcbda
assert len(string1) == len(string2)
return sum(abcbba != abcbda for abcbba , abcbda in zip(abcbba,abcbda))
if __name__ == "__main__":
    abcbba= hashlib.md5("abcbba".encode()).hexdigest()
    abcbda = hashlib.md5("abcbda".encode()).hexdisgest()
    print(hamming_distance(abcbba,abcbda))

