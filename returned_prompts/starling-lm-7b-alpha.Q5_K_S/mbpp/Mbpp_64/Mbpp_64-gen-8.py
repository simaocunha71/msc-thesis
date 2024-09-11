def subject_marks(marks):
    marks.sort(key = lambda x:x[1])
    return marks

# Testing the function
marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(subject_marks(marks))


# Expected Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



"""
We can sort a list of tuples by the value of a particular attribute of the tuple, in this case, the second attribute.

We can do this by using the lambda function as a key to the sort function. The lambda function returns the second attribute of the tuple, and the sort function sorts the list of tuples based on this attribute.

In the provided solution, the lambda function is defined as lambda x:x[1]. This means that for each tuple x in the list, the lambda function returns the second attribute of the tuple (i.e., x[1]).

The sort function is then used to sort the list of tuples based on the values returned by the lambda function. The sorted list is returned as the result of the function.
"""

# Python3 program to print Fibonacci series in O(log n) 

# Function to calculate the nth Fibonacci number 
def fibonacci(n): 

    # Initialize the array with 0 and 1 
    fib = [0, 1] 

    # Check if n is not in the array 
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 

        # Check if n is less than last element of array 
        while(fib[-1] < n): 
            fib.append(fib[-1] + fib[-2]) 

        # Return the Fibonacci number 
        return fib[-1] 

# Driver Program 
n = 10
print(fibonacci(n)) 

#