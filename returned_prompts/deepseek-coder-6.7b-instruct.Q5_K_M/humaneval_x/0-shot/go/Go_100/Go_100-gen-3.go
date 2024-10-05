
	stones := make([]int, n)

	for i := 0; i < n; i++ {
		if n%2 == 0 {
			stones[i] = n + 2*i
		} else {
			stones[i] = n + 2*i
		}
	}

	return stones
}

// MakeAPile(3) => [3, 5, 7]
// MakeAPile(4) => [4, 6, 8, 10]
// MakeAPile(5) => [5, 7, 9, 11, 13]

```


## 3.

```go

