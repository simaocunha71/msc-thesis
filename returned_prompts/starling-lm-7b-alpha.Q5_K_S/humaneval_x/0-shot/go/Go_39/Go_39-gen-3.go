	if n == 1 {
		return 2
	}
	if n == 2 {
		return 3
	}

	f := 4
	for i := 3; i < n; i++ {
		f += 6
		if math.Sqrt(float64(f))%1.0 == 0 {
			continue
		}

		if isPrime(f) {
			return PrimeFib(i)
		}

	}

	return PrimeFib(n)
}

func isPrime(n int) bool {
	if n == 2 {
		return true
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}

/*
The first few prime fibonacci numbers are 2, 3, 5, 13, 89, 233, 1586, 102322, ...

To generate the first few prime fibonacci numbers, we can follow these steps:

1. Initialize the first few Fibonacci numbers: 0, 1, 1, 2, 3, 5, ...
2. Check if each Fibonacci number is prime. If it's not prime, continue to the next Fibonacci number. If it's prime, return the Fibonacci number.
3. If we reach the end of the list of Fibonacci numbers without finding a prime Fibonacci number, return the last number in the list.

To check if a number is prime, we can follow these steps:

1. If the number is less than 2, return false because 0 and 1 are not prime.
2. If the number is 2, return true because 2 is the smallest prime number.
3. Check if the number is divisible by any number from 2 to the square root of the number. If the number is divisible by any of these numbers, return false because the number is not