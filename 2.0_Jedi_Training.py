'''
Sign your name: Tanner Evitts

1.) How do you enter a single line comment in a program? Give an example.

Use a #

2.) Enter a=2 and b=5 in the Python Console window and then all of the following. 
What are the outputs? If the output is an error record the error and try to determine what the error is!
'''
a=2
b=5

print(b/a) # 2.5
print(b//a) # 2
print(b**a) # 25
print(b%a) # 1
print(a+b) # Error B is not defined after fixed 7
print(type(42)) # int
print(type(42.0)) # float
print(type("C3PO")) # str
print(type(True)) # bool

'''
3.) What is the final output of (a) and type(a) if you enter the following 5 lines
into the Python Console Window?
'''
a=2
a*=10
a/=2
a+=12
a-=7
a
type(a)
# a is 15
'''
4.) What is the mistake in the following code. Fix it!
'''
x,y=(4,5)
a=3*(x+y)
print(a)
# there is spaces between the equal and plus sign sign in line 39 and 40 and there was no multiplication
# sign between the parnthasees and 3
'''
5.) What is the mistake in the following code so it will calculate the average. Fix it!
'''
x,y,z =(3,4,5)
ave=(x+y+z/3)
print(ave)
# there was no parenthasees around the equation