'''
Sign your name: Oded Harazi

1.) How do you enter a single line comment in a program? Give an example.
#You put a hashtag/pound before the comment

2.) Enter a=2 and b=5 in the Python Console window and then all of the following. 
What are the outputs? If the output is an error record the error and try to determine what the error is!
#B was undefined.
'''
a=2
b=5
print(b/a)
print(b//a)
print(b**a)
print(b%a)
#print(a+B) #B is undefined
print(type(42))
print(type(42.0))
print(type("C3PO"))
print(type(True))
'''

3.) What is the final output of (a) and type(a) if you enter the following 5 lines
into the Python Console Window?
'''
a=2
a*=10
a/=2
a+=12
a-=7
print(a) #15 - Correct prediction
print(type(a)) #Integer - Incorrect prediction
'''

4.) What is the mistake in the following code. Fix it!
'''
x,y=4,5 #Shouldn't have parenthesis
a=3*(x+y) #No multiplication sign
print(a) #forgot the "print()"
'''

5.) What is the mistake in the following code so it will calculate the average. Fix it!
'''
x,y,z=3,4,5 #shouldn't have parenthesis around the variables
ave=(x+y+z)/3 #missing parenthesis
print(ave) #No "print()"
