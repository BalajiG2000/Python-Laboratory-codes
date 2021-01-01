Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a={1:10,2:20,3:30,4:40}
>>> print a
{1: 10, 2: 20, 3: 30, 4: 40}
>>> b={'one':1,'two':2,'three':3,'four':4}
>>> print b
{'four': 4, 'three': 3, 'two': 2, 'one': 1}
>>> b.keys()
['four', 'three', 'two', 'one']
>>> b.values()
[4, 3, 2, 1]
>>> b.get(‘two’)
SyntaxError: invalid syntax
>>> b.get("two")
2
>>> b. update({'five':5})
>>> print b
{'four': 4, 'three': 3, 'five': 5, 'two': 2, 'one': 1}
>>> b={
