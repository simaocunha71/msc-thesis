Here is a Go solution that uses a slice to store the result and iterates over the input list to insert the delimiter:

```go
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)+len(numbers)-1)
    for i, n := range numbers {
        result = append(result, n)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```

This function creates a new slice with an initial capacity equal to the length of the input list plus the number of delimiters needed (which is one less than the length of the input list). Then, it iterates over the input list, appending each element to the result slice. If it's not the last element in the input list, it appends the delimiter as well. Finally, it returns the result slice.