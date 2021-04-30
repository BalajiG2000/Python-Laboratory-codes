Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a="this is super wierd"
>>> a.split()
['this', 'is', 'super', 'wierd']
>>> count(a)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined
>>> print count(a)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print count(a)
NameError: name 'count' is not defined
>>> 
c=0
for i in a:
	c+=1
	
>>> c
0
>>> count("a")

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    count("a")
NameError: name 'count' is not defined
>>> split()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    split()
NameError: name 'split' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>>  a="this is super wierd"
 
  File "<pyshell#9>", line 2
    a="this is super wierd"
    ^
IndentationError: unexpected indent
>>> a="this is super wierd"
>>> a.find("is")
2
>>> a.
SyntaxError: invalid syntax
>>> a.capitalize()
'This is super wierd'
>>> a.islower()
True
>>> a.isupper()
False
>>> a.upper()
'THIS IS SUPER WIERD'
>>> a.lower()
'this is super wierd'
>>> 
