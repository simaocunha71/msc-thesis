
    sum := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i] % 2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

## Hints

- Remember that array indexing in Go starts from 0, so the first element is at index 0, the second at index 1, etc.
- The condition `i % 2 == 1` checks if the index `i` is odd.
- To check if the element at an odd index is even, you can use the modulo operator `%` to get the remainder of the division by 2. If the remainder is 0, the number is even.

## Notes

- The problem statement seems to be a bit ambiguous. It says to add the even elements that are at odd indices, but it doesn't clarify whether the index or the value is even. In this solution, we're assuming the index is even.
- If the problem statement means to add the even elements at odd indices, you just need to change `i % 2 == 1` to `lst[i] % 2 == 0`.

## Test Cases

```go
func TestAdd(t *testing.T) {
    type args struct {
        lst []int
    }
    tests := []struct {
        name string
        args args
        want int
    }{
        {name: "Example 1", args: args{lst: []int{4, 2, 6, 7}}, want: 2},
        {name: "Example 2", args: args{lst: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}}, want: 6},
        {name: "Example 3", args: args{lst: []int{2, 3, 4, 5, 6, 7, 8, 9, 10}}, want: 4},
        {name: "Example 4", args: args{lst: []int{1}}, want: 0},
        {name: "Example 5",