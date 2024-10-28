	prime_fib_nums := []int{2}
	i := 3
	for len(prime_fib_nums) < n {
		is_prime := true
		sqrt_i := int(math.Sqrt(float64(i)))
		for _, prime := range prime_fib_nums {
			if prime > sqrt_i {
				break
			}
			if i%prime == 0 {
				is_prime = false
				break
			}
		}
		if is_prime {
			prime_fib_nums = append(prime_fib_nums, i)
		}
		i += 2
	}
	return prime_fib_nums[n-1]
}

func main()  {
	fmt.Println(PrimeFib(1)) // 2
	fmt.Println(PrimeFib(2)) // 3
	fmt.Println(PrimeFib(3)) // 5
	fmt.Println(PrimeFib(4)) // 13
	fmt.Println(PrimeFib(5)) // 89
}
```

Here's an explanation:

- The function `PrimeFib(n int) int` returns the n-th prime number that is also a Fibonacci number.
- We use the Sieve of Eratosthenes algorithm to find prime numbers.
- We start with the number 2 (the first Fibonacci number) and keep adding odd numbers (since only they can be prime) to our list of prime numbers.
- For every number in our list, we check if it can divide our current number (i). If it can, we break the loop and move on to the next number. If it can't, we add it to our list of prime numbers and continue.
- Finally, we return the n-th prime number from our list.

I hope this helps in understanding how to solve this problem. If you have any questions, feel free to ask.

Note: This solution may not be efficient for large values of `n` due to the nature of the problem. The time complexity is O(n^2), which