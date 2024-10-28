```
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)+len(numbers)-1)
    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```



The goal is to create a new list where every two consecutive elements from the original list are separated by the given delimiter.

Here is the solution in Go:
```
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)+len(numbers)-1)
    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```
This function creates a new slice `result` with an initial capacity of `len(numbers)+len(numbers)-1`. This is because we will be adding `len(numbers)` elements from `numbers` and `len(numbers)-1` delimiters.

Then it iterates over the `numbers` slice. For each element, it appends the element to `result`. If it's not the last element, it also appends the delimiter.

Finally, it returns the `result` slice.

For example, if we call `Intersperse([1, 2, 3], 4)`, the function will return `[1, 4, 2, 4, 3]`. If we call `Intersperse([], 4)`, it will return `[]`. If we call `Intersperse([1], 4)`, it will return `[1]`. If we call `Intersperse([1, 2], 4)`, it will return `[1, 4, 2]`. And so on.