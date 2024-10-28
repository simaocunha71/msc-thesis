Here is the solution:
```go
func SortEven(l []int) []int {
    even := make([]int, 0, len(l)/2)
    for i := 0; i < len(l); i += 2 {
        even = append(even, l[i])
    }
    sort.Ints(even)
    result := make([]int, 0, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            result = append(result, even[i/2])
        } else {
            result = append(result, l[i])
        }
    }
    return result
}
```
Here's a breakdown of the solution:

1. We create a new slice `even` to hold the even-indexed elements of `l`. We use a loop to iterate over `l` and append the even-indexed elements to `even`.
2. We sort the `even` slice using the `sort.Ints` function from the `sort` package.
3. We create a new slice `result` to hold the final result. We use a loop to iterate over `l` and append the elements to `result`. If the index `i` is even, we append the corresponding element from `even` to `result`. If `i` is odd, we append the corresponding element from `l` to `result`.
4. Finally, we return the `result` slice.

You can test this function with the examples you provided:
```go
fmt.Println(SortEven([]int{1, 2, 3})) // [1, 2, 3]
fmt.Println(SortEven([]int{5, 6, 3, 4})) // [3, 6, 5, 4]
```I hope this helps! Let me know if you have any questions.