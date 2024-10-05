```go
	sort.Ints(l)
	length := len(l)
	mid := length / 2
	if length%2 == 0 {
		return float64(l[mid-1]+l[mid]) / 2
	}
	return float64(l[mid])
}
```

