
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fib(10))
print(fib(1))
print(fib(8))
"""

# Python program for nth Fibonacci number

# Function to find nth Fibonacci number
def Fibonacci(n):
	
	# Check if n is negative
	if n<0 or type(n)!=int:
		print("Incorrect input")
		
	# Check if n is 0
	elif n==0:
		return 0
	
	# Check if n is 1 or 2
	elif n==1 or n==2:
		return 1
	
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
	
# Test Function
print(Fibonacci(10))
print(Fibonacci(1))
print(Fibonacci(8))

# Python program for nth Fibonacci number

# Function to find nth Fibonacci number
def Fibonacci(n):
	
	# Check if n is negative
	if n<0 or type(n)!=int:
		print("Incorrect input")
		
	# Check if n is 0
	elif n==0:
		return 0
	
	# Check if n is 1 or 2
	elif n==1 or n==2:
		return 1
	
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
	
# Test Function
print(Fibonacci(10))
print(Fibonacci(1))
print(Fibonacci(8))
<jupyter_output>
55
1
21