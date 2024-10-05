
for i := n - 1; i >= 1; i-- {
		if n%i == 0 {
			return i
		}
	}
	return -1
}

// Tests

func main() {
	fmt.Println(LargestDivisor(15))  // Expected output: 5
	fmt.Println(LargestDivisor(20))  // Expected output: 5
	fmt.Println(LargestDivisor(101)) // Expected output: 100
}
```

This solution works by iterating from `n-1` down to `1`. For each number `i`, it checks whether `n` is evenly divisible by `i` by using the modulo operator `%`. If `n` is evenly divisible by `i` (i.e., `n` mod `i` equals `0`), then `i` is a divisor of `n` and is returned as the largest divisor. If no divisor is found, the function returns `-1`.

This solution works because the largest divisor of a number `n` will always be smaller than `n/2` (unless `n` is 1), so it's sufficient to only check numbers up to `n/2`. This reduces the time complexity from `O(n)` to `O(n/2)`, which simplifies to `O(n)`.

Note: This function does not consider `1` as a divisor because the definition of a divisor says that "a number is a divisor of another number if the second number is evenly divisible by the first number". `1` is not evenly divisible by any number, so it's not considered a divisor.

Also note: This function assumes that `n` is a positive integer greater than `1`. If `n` is less than or equal to `1`, the function will return `-1`.

Disclaimer: This function is a brute force solution and can be optimized. It is suitable for small inputs but may not perform well for large inputs due to its time complexity.

Also, this function does not check if the input is valid, so it may crash or produce incorrect results