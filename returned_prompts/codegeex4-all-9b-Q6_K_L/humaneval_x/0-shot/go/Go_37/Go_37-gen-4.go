```go
func SortEven(l []int) []int {
	if len(l) == 0 {
		return l
	}
	even := []int{}
	for i := 0; i < len(l); i += 2 {
		even = append(even, l[i])
	}
	sort.Ints(even)
	j := 0
	for i := 0; i < len(l); i += 2 {
		l[i] = even[j]
		j++
	}
	return l
}
```