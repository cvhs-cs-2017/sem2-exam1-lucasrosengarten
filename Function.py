"""Define a function that will take a parameter, n, and triple it and return
the result"""
def triple(n):
    n = 3 * n
    return n
print(triple(5))




"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """
def Triple(n):
    print("Enter number")
    n = int(input())
    n = n * 3
    return n
print (Triple(3))
