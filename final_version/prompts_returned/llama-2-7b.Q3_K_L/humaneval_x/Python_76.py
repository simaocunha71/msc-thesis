
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    return x ** n == int(x**n)
def main():    
    print("Enter a number.")
    n = eval(input())
    print('Simple Power of ' + str(n))
    for i in range(1, 6):
        for j in range(20):
            if is_simple_power(i**j, n) == True:
                print("Number: " + str(i**j) + ", is a simple power of " +str(n))
    return False
main()