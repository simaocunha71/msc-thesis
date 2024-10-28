
The code you have posted is not complete, there are several parts missing, like the input to the functions and the actual function signatures. I will try to complete the code and provide some comments.
# Q1
To check if there are any two numbers closer to each other than given threshold, we can sort the list of numbers and then check the difference between each pair of consecutive numbers.

```go
import (
    "sort"
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    sort.Float64s(numbers)
    for i := 0; i < len(numbers)-1; i++ {
        if math.Abs(numbers[i]-numbers[i+1]) < threshold {
            return true
        }
    }
    return false
}
```

# Q2
To separate the groups of parentheses, we can iterate over the input string and count the depth of nested parentheses. When the depth becomes 0, we add the current group to the result.

```go
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

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}
```

# Q3
To truncate a number, we can use the `math.Mod` function to get the decimal part of the number.

```go
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}
```

# Q4
To get the sum of the upper characters only' ASCII codes, we can iterate over the string and check if the character is an upper case letter. If it is, we add its ASCII code to the result.

```go
func Digitsum(x string) int {
    result := 0
    for _,