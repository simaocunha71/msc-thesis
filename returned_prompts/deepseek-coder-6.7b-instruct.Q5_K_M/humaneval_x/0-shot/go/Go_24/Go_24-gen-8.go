
	result := 0
	for i := 1; i < n; i++ {
		if n%i == 0 {
			result = i
		}
	}
	return result
}

// The program starts by initializing result to 0. Then it starts a loop which iterates over the numbers from 1 to n - 1. If n is divisible by the number, it sets result to that number. This means that by the end of the loop, result will be the largest number that divides n evenly.

```

## Q2

```go

