
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # base case
    if a <= 3 : return True

    # loop to check conditions
    for i in range (4,a+1):
        if is_prime(i) and a%i == 0:
            print("The number is ", a," *",i)

return False
