
Here are the solutions to your problems:
1. HasCloseElements
Your function is correct, but there is a small optimization that can be done. Instead of using two nested loops to compare every pair of numbers, you can sort the array first and then check the difference between consecutive numbers. This way, you only need to iterate through the array once.
Here is the optimized function:
```go
import (
    "sort"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    sort.Float64s(numbers)
    for i := 1; i < len(numbers); i++ {
        if numbers[i]-numbers[i-1] < threshold {
            return true
        }
    }
    return false
}
```

2. SeparateParenGroups
Your function is also correct, but there is a small mistake in the loop. You should decrement the current depth when you encounter a closing parenthesis, not an opening parenthesis. Here is the corrected function:
```go
import (
    "strings"
)

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_string = append(current_string, c)

            if current