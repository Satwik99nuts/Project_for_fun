# So here now I will make a scientific calculator

##
import math # for using log and trigonometric functions
import sympy as sp #to do integration and differentiation.
print("Welcome to the Calculator!")
print("How many numbers do you want to operate on?")
print("(NOTE:- If You want to do the square, cube or root of a number, just input 1 number in the below section.)")
num_count = int(input("Enter the number of numbers: "))
##
number = []  #so here i have made a list for storing the users numbers
for i in range(num_count):
    num = int(input("Enter "+ str(i+1) +" number ")) #here we have to make i a string before concatenating it to the string, that's why we have used str(i+1) here.
    #also str(i+1) is used here beacause indexing in python starts from 0 and we humans start from 1, so if num_count= 4, so python will go up to 0,1,2,3 and 4 th number will be left but with str+1, this thing vanishes.
    
    number.append(num) #to store each number in the list.
##  SUM
def Sum(number):
    total = 0
    for j in number: #i here gives us the index number and not the actual numbers inpurtted by the user.
        total +=j
    return total #Always return the value from functions that calculate something, and print it outside the function. That keeps your code cleaner and easier to maintain. If we don't use it here, we can't use the sum outside of the function anywhere else in the program.

## DIFFERENCE
def diff(number):
    difference =number[0] #for difference, we usually subtract the second number from the first number and then third number and then so on.
    for d in number[1:]: #here we are subtracting the first number from the second number and that's why i have used number[1:], so that the number can't subtract itself from itself.
        difference -= d 
    return difference

## MULTIPLY
def multiply(number):
    mult = 1
    for m in number:
        mult *= m
    return mult
##  DIVISION
def division(number): #here i am assuming that the order in which the numbers are written is the order in which they are getting divided.
    if len(number)<2:
        print("Can't divide in this case")
    try:
        dividend = number[0]
        print("The divident among the numbers is: ", dividend) #her we can't use + in between the string and dividend as dividend is a int or float and the para is a string. So we have to write a comma(,) in between them.
        for divisor in number[1:]: #here number[1:] is given because we want to divide the first number by the rest of numbers and not the first number by itself.
            dividend = dividend/divisor
        return dividend #as the quotient will become the new dividend and so on. And the dividend will be the new answer.
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
##  SQUARE
def square(number):
    for s in number:
        print("The Square of given number is: ",s*s)
## CUBE
def cube(number):
    for c in number:
        print("The Cube of given number is: ",c*c*c)
## ROOT
def root(number):
    for r in number:
        print("The Root of the given number is: ", r**(0.5))
## FCTORIAL
def factorial(number):
    results = [] # to store the factorial results.
    for f in number: # here i want to iterate through each number in the numbers list, for ex if number =[4,5], so for iterating through  number, we need to run this loop.
        fact = 1 # as fact can not be zero.
        for o in range(1,f+1): # here I am taking a range of that particular number.
            fact *= o #here we are multiplying 1 with every number in the range and then storing it in the same fact variable and again the loop starts and stores and multiplies again. 
        results.append(fact) # to store the factorial results in results list.
    return results #to return list of factorial.
##
print("\nSelect the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Cube")
print("7. Root")
print("8. Factorial")

choice = int(input("Enter your Choice(between 1-4) = "))
if choice < 5:
    print("Valid Operation Chosen")
##
operation_list={1:Sum, 2:diff,3:multiply,4:division} 
if choice == 1:
    print(Sum(number))
elif choice == 2:
    print(diff(number))
elif choice ==3:
    print(multiply(number))
elif choice ==4:
    print(division(number))
elif choice ==5:
    print(square(number))
elif choice ==6:
    print(cube(number))
elif choice ==7:
    print(root(number))
elif choice ==8:
    print(factorial(number))
else:
    print("Invalid Choice Selected")
