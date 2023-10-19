Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def generate_integer(level):
...     if level == 1:
...         return random.randint(0, 9)
...         #The randint() method returns an integer number selected element from the specified range.
...     elif level == 2:
...         return random.randint(10, 99)
...     elif level == 3:
...         return random.randint(100, 999)
...     else:
	    raise ValueError("Invalid level")
