
Here are the solutions for the problems you've posted:

HasCloseElements:
This problem involves checking if any two numbers in a given list are closer to each other than a specified threshold. To solve this, you can iterate through the list and compare each pair of numbers. If the absolute difference between any two numbers is less than the threshold, then return true. If no such pair is found, return false.

```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```

SeparateParenGroups:
This problem involves separating groups of nested parentheses from a given string. To solve this, you can iterate through the string and keep track of the current depth of parentheses. Whenever you encounter an opening parenthesis, increase the depth and add it to the current string. Whenever you encounter a closing parenthesis, decrease the depth and add it to the current string. If the depth becomes zero, it means a group is complete and you can add it to the result list. Finally, return the result list.

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

TruncateNumber:
This problem involves truncating a given floating-point number to its decimal part. To solve this, you can use the math.Mod function to get the remainder of the number when divided by 1. This will give you the decimal part of the number.

```go
func