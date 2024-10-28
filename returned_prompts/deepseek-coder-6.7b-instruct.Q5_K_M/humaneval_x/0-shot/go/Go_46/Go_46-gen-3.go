
// Base cases
if n == 0 {
	return 0
}
if n == 1 {
	return 0
}
if n == 2 {
	return 2
}
if n == 3 {
	return 0
}

// Initializing the array to store the Fib4 numbers
fib := make([]int, n+1)
fib[0] = 0
fib[1] = 0
fib[2] = 2
fib[3] = 0

// Filling up the array
for i := 4; i <= n; i++ {
	fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
}

return fib[n]
}

// The time complexity of the function is O(n) as it iterates over the range from 4 to n. The space complexity is also O(n) as it uses an array of size n+1 to store the Fib4 numbers.
```

### Task 2:

Write a function that takes a string as an argument and returns a dictionary that contains the count of each character in the string.

```python
