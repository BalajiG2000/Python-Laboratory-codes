Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_string = 'Hello'
>>> print my_string
Hello
>>> 
>>> my_string = "Hello"
>>> print my_string
Hello
>>> my_string = '''Hello'''
>>> print my_string
Hello
>>> my_string = """Hello, welcome to
the world of Python"""
>>> print my_string
Hello, welcome to
the world of Python
>>> default_order = "{}, {} and {}".format('ECE','MEC','CSE')
>>> print '\n--- Default Order ---'

--- Default Order ---
>>> print default_order
ECE, MEC and CSE
>>> positional_order = "{1} in {0} is {2}".format('Guna','University','JUET')
>>> print '\n--- Positional Order ---'
print positional_order

--- Positional Order ---
>>> print positional_order
University in Guna is JUET
>>> keyword_order = "{r} has {j} and {u}".format(j='Jaypee',u='University',r='Raghogarh')
>>> print '\n--- Keyword Order ---'

--- Keyword Order ---
>>> 
>>> print keyword_order
Raghogarh has Jaypee and University
>>> my_string = input('Enter your string in cotes :' )
Enter your string in cotes :'qwerty'
>>> print 'the string {0} has length {1}'.format(my_string,len(my_string))
the string qwerty has length 6
>>> my_string = raw_input('Enter your string without cotes : ' )
Enter your string without cotes : qwerty
>>> print 'the string {0} has length {1}'.format(my_string,len(my_string))
the string qwerty has length 6
>>> 
