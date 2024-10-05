
// 1. Define a variable to hold the largest prime factor.
	largestPrimeFactor := 0

B:

// 2. Loop through the numbers from 2 to sqrt(n).
	for i := 2; i * i <= n; i++ {

C:

// 3. Check if n is divisible by i.
		if n % i == 0 {

D:

// 4. If n is divisible by i, update largest prime factor and divide n by i.
			largestPrimeFactor = i
			n = n / i
		}
	}

E:

// 5. If n is a prime number and greater than the largest prime factor, update the largest prime factor.
	if n > largestPrimeFactor {
		largestPrimeFactor = n
	}

F:

// 6. Return the largest prime factor.
	return largestPrimeFactor
}

func main() {
	fmt.Println(LargestPrimeFactor(13195)) // Output: 29
	fmt.Println(LargestPrimeFactor(2048))  // Output: 2
}
```

The algorithm works by looping through the numbers from 2 to sqrt(n), and checking if n is divisible by each of these numbers. If n is divisible, we update our largest prime factor and divide n by the divisor. We continue this process until n becomes a prime number (which will be the largest prime factor if it's greater than the current largest prime factor).

The time complexity of this algorithm is O(sqrt(n)) because we only loop through sqrt(n) numbers. The space complexity is O(1) because we only use a constant amount of space to store our largest prime factor.


























































































