	evenIdx := make([]int, 0)
	evenVal := make([]int, 0)

	for i := 0; i < len(l); i+=2 {
		evenIdx = append(evenIdx, i)
		evenVal = append(evenVal, l[i])
	}

	sort.Ints(evenVal)

	for i := 0; i < len(evenIdx); i++ {
		l[evenIdx[i]] = evenVal[i]
	}

	return l
}
```

## Answer 2:
```go
