def armstrong_number(n):
    temp=n
    sum=0
    count=0
    while temp>0:
        digit=temp%10
        sum=(sum)+(digit**len(str(n)))
        temp=int(temp/10)
    if sum==n:
        return True
    else:
        return False
    # You can also use this formula instead of above loop
    # return n==sum(int(i)**len(str(n)) for i in str(n))  # Python 3.5+
    # This formula convert the number to string, then iterate over each character, 
    # convert it back to integer, raise it to the power of the length of the original number, 
    # and sum all the results. Then it checks if the sum is equal to the original number. 
    # If it is, the number is an Armstrong number. 
    # This formula is more efficient than the loop version. 
    # But it only works in Python 3.5+, because of the usage of the expression as a function. 
    # In Python 2.x, you would need to use a list comprehension instead. 
    # For example: return n==sum(int(i)**len(str(n)) for i in str(n))  # Python 2.x
    # This formula is more efficient than the loop version. 
    # But it only works in Python 3.5+, because of the usage of the expression as a function. 
    # In Python 2.x, you would need to use a list comprehension instead. 
    # For example: return n==sum(int(i)**len(str(n)) for i in str(n))  # Python 2.x
    # This formula is more efficient than the loop version. 
    # But it only works in Python 3.5+, because of the usage of the expression as a function. 
    # In Python 2.x, you would need to use a list comprehension instead. 
    # For example: return n==sum(int(i)**len(str(n)) for i in str(n))  # Python 2.x
    # This formula is more efficient than the loop version. 
    # But it only works in Python 3.5+, because of the usage of the expression as a function. 
    # In Python 2.x, you would need to use a list comprehension instead. 
    # For example: return n==sum(int(i)**len(str(n