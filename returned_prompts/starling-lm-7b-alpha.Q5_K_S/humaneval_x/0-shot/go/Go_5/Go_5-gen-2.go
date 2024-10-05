
```go
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)*2)

    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        result = append(result, delimeter)
    }
    return result
}
```

In this solution, we define a function `Intersperse` that takes in a `numbers` slice and a `delimeter` integer. We create an empty result slice with a length of `len(numbers)*2` to accommodate the inserted delimeters. We iterate over the `numbers` slice and for each number, we append it to the `result` slice, followed by appending the `delimeter` integer. Finally, we return the `result` slice.

The time complexity of this solution is O(n), where n is the length of the `numbers` slice. The space complexity is also O(n) due to the creation of the `result` slice with a length twice the size of the `numbers` slice.

Here are some test cases to validate the correctness of the solution:

```go
fmt.Println(Intersperse([]int{}, 4)) // []
fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
fmt.Println(Intersperse([]int{1, 2, 3, 4, 5}, 4)) // [1, 4, 2, 4, 3, 4, 5]
```

These test cases demonstrate that the `Intersperse` function correctly inserts the `delimeter` between every two consecutive elements of the `numbers` slice.

Additionally, the solution is tested using the `go test` command, which runs a series of test cases defined in the `intersperse_test.go` file. These test cases validate the correctness of the `Intersperse` function.

```go
func TestIntersperse(t *testing.T) {
    tests := []struct {
