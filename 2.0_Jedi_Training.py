'''
Sign your name: Matthew Hammerand

1.) How do you enter a single line comment in a program? Give an example.
With a # before the comment

2.) Enter a=2 and b=5 in the Python Console window and then all of the following. 
What are the outputs? If the output is an error record the error and try to determine what the error is!
'''
a=2
b=5

print(b/a)  #2.5
print(b//a) #2
print(b**a )    #25
print(b%a)  #1
#print(a+B)  #error, the B is not defined because it is B and not b
print(type(42)) #class=int
print(type(42.0))   #class=float
print(type("C3PO")) #class=str
print(type(True))   #class=bool

'''
3.) What is the final output of (a) and type(a) if you enter the following 5 lines
into the Python Console Window?
'''
a=2
a*=10
a/=2
a+=12
a-=7

print(a)    #15.0
print(type(a))  #class=float

'''
4.) What is the mistake in the following code. Fix it!
'''
#no * sign
x,y=(4,5)
a=3*(x+y)
print(a)

'''
5.) What is the mistake in the following code so it will calculate the average. Fix it!
'''
#it was using order of operations and dividing by z by 3 first
x,y,z=(3,4,5)
ave=(x+y+z)/3
print(ave)



