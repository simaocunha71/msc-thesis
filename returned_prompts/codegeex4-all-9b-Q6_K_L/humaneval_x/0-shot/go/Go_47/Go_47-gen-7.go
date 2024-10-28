```go
func Median(l []int) float64 {
	sort.Ints(l)
	mid := len(l) / 2
	if len(l)%2 == 0 {
		return float64(l[mid-1]+l[mid]) / 2.0
	}
	return float64(l[mid])
}
```