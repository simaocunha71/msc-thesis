```go
func GetPositive(l []int) []int {
    var result []int
    for _, num := range l {
        if num > 0 {
            result = append(result, num)
        }
    }
    return result
}
```


This function takes a slice of integers as input and returns a new slice containing only the positive numbers from the input slice.

Here's how it works:

1. We initialize an empty slice `result` that will store the positive numbers.
2. We iterate over the input slice `l` using a range loop.
3. For each number `num` in the input slice, we check if it's greater than 0 using the condition `num > 0`.
4. If the number is positive, we append it to the `result` slice using the `append` function.
5. Finally, we return the `result` slice, which contains only the positive numbers from the input slice.

You can test this function with the examples you provided:
```go
result := GetPositive([]int{-1, 2, -4, 5, 6})
fmt.Println(result) // [2, 5, 6]

result = GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
fmt.Println(result) // [5, 3, 2, 3, 9, 123, 1]
```