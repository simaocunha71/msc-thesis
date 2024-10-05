```go
	// copy the input list
	l2 := make([]int, len(l))
	copy(l2, l)

	// find the even indices
	evenIndices := make([]int, len(l)/2)
	for i := 0; i < len(evenIndices); i++ {
		evenIndices[i] = 2*i
	}

	// sort the values at the even indices
	sort.Ints(l2[evenIndices[0] : evenIndices[len(evenIndices)-1]+1])

	return l2
}
```

