```go
func ChooseNum(x, y int) int {
	if x > y {
		return -1
	}
	for x <= y {
		if x%2 == 0 {
			return x
		}
		x++
	}
	return -1
}
```