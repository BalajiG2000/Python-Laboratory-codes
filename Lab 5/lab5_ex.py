Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> b={4:"four",3:"three",2:"two"}
print b
>>> 
>>> 
>>> print b
{2: 'two', 3: 'three', 4: 'four'}
>>> b.update({5:"five"})
>>> print b
{2: 'two', 3: 'three', 4: 'four', 5: 'five'}
>>> for i,j in b.iteritems():
	    print i,
	    print “: “,j
	    
SyntaxError: invalid syntax
>>> 
