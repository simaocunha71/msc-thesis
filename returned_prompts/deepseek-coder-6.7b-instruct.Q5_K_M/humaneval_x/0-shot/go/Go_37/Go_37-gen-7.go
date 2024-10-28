	even := make([]int, len(l)/2)
	odd := make([]int, len(l)/2)

	for i := 0; i < len(l); i += 2 {
		even[i/2] = l[i]
	}
	for i := 1; i < len(l); i += 2 {
		odd[i/2] = l[i]
	}
	sort.Ints(even)

	for i := 0; i < len(l)/2; i++ {
		l[2*i+1] = odd[i]
		l[2*i] = even[i]
	}
	return l
}
```

## Solution:

```go
