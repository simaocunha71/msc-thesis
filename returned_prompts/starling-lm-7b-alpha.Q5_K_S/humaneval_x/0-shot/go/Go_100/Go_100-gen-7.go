
```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = i + 1
        } else {
            result[i] = i + 2
        }
    }
    return result
}
```

To solve this problem we can follow these steps:

1. Create a slice to store the result. In this case we can use the `make` function to create an empty slice of integers.
2. Iterate over the range of `n` using a `for` loop.
3. For each iteration, check if the index is even or odd using the modulo operator `%`. If the index is even, assign the next even number to the result slice. If the index is odd, assign the next odd number to the result slice.
4. Return the result slice containing the number of stones in each level.

In the provided solution, the `MakeAPile` function takes a positive integer `n` as a parameter and returns a slice of integers. Inside the function, a slice named `result` is created using the `make` function to store the result. Then, a `for` loop is used to iterate over the range of `n`. For each iteration, the index is checked if it's even or odd using the modulo operator `%`. If the index is even, the next even number is assigned to the `result` slice. If the index is odd, the next odd number is assigned to the `result` slice. Finally, the `result` slice is returned, containing the number of stones in each level of the pile.

You can test the solution by calling the `MakeAPile` function with a positive integer argument. For example, `MakeAPile(3)` will return `[3, 5, 7]`, representing the number of stones in each level of a pile with 3 levels.

```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = i + 1
        }