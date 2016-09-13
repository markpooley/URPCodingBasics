#Week1
print type(1)
print type(1.0)
print type('this is some text')
print type([1,2,3,5])

"""
#accessing a list
ls = [1,2,3,4]
print ls[0] #access first element of list
print ls[:2] #access first two elements, that is "up to" but not including the third element
print ls[2:3] #starting at third element, access up to the fourth
print ls[2:] #access everything beyond the third element

#List operations
ls.append(6) #append element to end of list
print ls
ls.pop(2) #remove 3rd element of list
print ls
ls.insert(2,7) #insert 7 ad the third index
print ls
ls.sort() #sort list ascending
print ls
ls = ls[:4] #create new list as subset of original
print ls
l = len(ls) #get list length
print 'Length of list "ls" is: {0}'.format(l)

#you can access indices of strings to!
s = 'This is a string'
print s[0]
print s[:6] #access everything up to before the 7th character
print s[4:] #access everything beyond 5th character
print s[-1] #access last element




#maths
print 2 / 3 # two divided by three
print 3 % 2 #remainder of 3 /2 which is 1
print 2 + 2
print 2 * 3
print 2 ** 3 # first number raised to the power of the second

#string operations

print 'this is some text' + ' this is some more text' #simple concantenation
print '%s is a place holder for %s' %('percent sign','text to be entered later') #using % placeholder
print "{0} can also be used as a place holder using the {1} function".format('brackets','format') #using format function - my favorite
print 'You an add a number to a string if you use str(number): ' + str(2.0) + '.' #concantenate number into string using str() conversion

#-------------------------
#functions!
#-------------------------

#this will take some string and a number and return
#a setence along with that number multiplied by 10
def func(string, number):
    multi = number * 10 #multiply number by 10
    #take a look at what's going on here. we're converting a number to a string
    #and concantenating multiple strings to return one output from the function.
    s = str(number) + ' multiplied by 10 is: ' + str(multi) + "\nAlso, here's the text the function took as input: {0}".format(string)
    return s

print func('text',4)

def iffer(number):
    s = "{0} is ".format(number)#setup the string to return
    if number % 2 > 0: #if number divided by 2 has a remainder, then it's odd
        s = s + 'odd'
    else: #if the first if condition isn't satisfied, it's even
        s = s + 'even'
    return s

print iffer(3)
print iffer(12454)

#introduction to the "in" statement
def inner(numbers,target):
    #check if target is in the numbers list using "in" comparison.
    if target in numbers:
        answer = "yep!"
    else:
        answer = "nope!"
    return answer

ls = [1,2,3,4,5,6,7,8,9] # create a simple list
print inner(ls,3)
print inner(ls,12)

#introduction to elif and == comparison operator
#this function will check of a number is zero, odd, or even
def elifer(number):
    if number == 0:
        answer = 'number is zero'
    elif number % 2 == 0:
        answer = 'number is even'
    else:
        answer = 'number is odd'
    return answer

print elifer(0)
print elifer(43)
print elifer(78646)

#import a standard library included with Python
import random
#create random number between 0 and 10. 
#random access the library the "." access the class/module within that library
r = random.randint(0,10) 
print r
"""