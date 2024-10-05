```go
func Intersperse(numbers []int, delimeter int) []int {
    interspersed := make([]int, 0)
    for _, num := range numbers {
        interspersed = append(interspersed, num, delimeter)
    }
    if len(interspersed) > 0 {
        interspersed = interspersed[:len(interspersed)-1] // remove the last delimeter
    }
    return interspersed
}
```
