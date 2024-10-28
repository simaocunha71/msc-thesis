You can use the following code to solve the problem:

```go
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0)
    for i, num := range numbers {
        result = append(result, num)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```

This function takes two parameters: `numbers`, a slice of integers, and `delimeter`, an integer. It returns a new slice of integers with the `delimeter` inserted between every two consecutive elements of the input list.

The function uses a loop to iterate over the elements of the input list. For each element, it appends the element itself and the `delimeter` to the result slice. If the current element is the last element of the input list, it does not append the `delimeter` after it.

Finally, the function returns the result slice.