	var a, b = 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
		if b > 2 && isPrime(b) {
			return b
		}
	}
	return 0
}

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

/*
Fibonacci numbers are defined by the following recurrence relation:
F(0) = 0, F(1) = 1, and F(n) = F(n−1) + F(n−2) for n > 1.

This question is asking for the nth Fibonacci number that is also a prime number.

It is known that all Fibonacci numbers beyond the 4th are composite (i.e., not prime),
so we don't have to check for primality until F(4) = 3.

The first few prime Fibonacci numbers are: 2, 3, 5, 13, 89, ...

The solution uses two helper functions:

isPrime(n int) -> bool: Determines if the integer n is prime.
PrimeFib(n int) -> int: Returns the nth prime Fibonacci number.

The isPrime function checks if a number is prime by checking all numbers from 2 through the square root of n.
If n is divisible by any of these numbers, it is not prime.

The PrimeFib function generates the Fibonacci sequence until it finds a number that is prime.
It starts by initializing a and b to 0 and 1 respectively.
Then it generates the Fibonacci sequence by repeatedly swapping a and b, and setting a to the sum of the previous values of a and b.
If the generated Fibonacci number is greater than 2 and is prime, it returns the