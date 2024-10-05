
// Initialize a variable to keep track of the count of numbers above threshold
	count := 0

B:

// Iterate through the list
	for _, num := range l {

C:

// If the number is greater than threshold, increment count
		if num > t {
			count++
		}
	}

D:

// If the count is 0, all numbers are below threshold, return true
	if count == 0 {
		return true
	}

E:

// Otherwise, return false
	return false
}

```


### 4.1.3. Fibonacci
```go
