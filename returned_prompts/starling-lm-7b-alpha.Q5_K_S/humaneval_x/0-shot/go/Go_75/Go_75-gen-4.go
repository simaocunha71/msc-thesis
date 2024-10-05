
```go

import (
	"math"
)

func IsMultiplyPrime(a int) bool {
	prime := [100]bool{}
	for i := 2; i < 100; i++ {
		prime[i] = true
	}
	
	for i := 2; i*i < 100; i++ {
		if prime[i] == true {
			for j := i*i; j < 100; j += i {
				prime[j] = false
			}
		}
	}
	
	
	if a < 3 {
		return false
	}
	
	n := int(math.Floor(math.Sqrt(float64(a))))
	
	for i := 2; i <= n; i++ {
		if a%i == 0 {
			return prime[i] && prime[a/i]
		}
	}
	
	return prime[a]
}
```

Explanation:
This is a very basic implementation of the "Sieve of Eratosthenes" algorithm, which is used to find all prime numbers up to a certain limit. In this case, the limit is 100. The function then checks if the input number can be divided by 2 or 3. If it can, the function returns false. If not, it checks if the input number is a prime number. If it is, the function returns true.

This implementation is very basic and not efficient. It has a time complexity of O(n log(log n)), which is slower than more advanced algorithms like the Sieve of Eratosthenes, which have a time complexity of O(n log log n).

It is important to note that this implementation is not suitable for larger numbers than 100, as it would take too long to calculate all the prime numbers.

There are also other algorithms to check if a number is a product of prime numbers, such as the AKS primality test, but they are more complex and not necessary for this problem.

In summary, this implementation is a basic and inefficient solution to the problem, and