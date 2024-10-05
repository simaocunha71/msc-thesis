
```go
func Fibfib(n int) int {
	if n == 0 || n == 1 {
		return 0
	}
	if n == 2 {
		return 1
	}
	fibfib := make([]int, n+1)
	fibfib[0] = 0
	fibfib[1] = 0
	fibfib[2] = 1
	for i := 3; i <= n; i++ {
		fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
	}
	return fibfib[n]
}
```

Explanation:

First, we can handle the base cases, which are Fibfib(0) == 0, Fibfib(1) == 0, and Fibfib(2) == 1.

Then, we create a slice fibfib of size n + 1 to store the Fibfib numbers.

We initialize fibfib[0] and fibfib[1] to 0, and fibfib[2] to 1.

Next, we use a for loop to calculate the Fibfib numbers from index 3 to n. For each index i, we calculate the Fibfib number at index i by adding the Fibfib numbers at index i-1, i-2, and i-3. We store the result in fibfib[i].

Finally, we return the Fibfib number at index n from the fibfib slice.

This solution has a time complexity of O(n) because we only need to calculate each Fibfib number once.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

