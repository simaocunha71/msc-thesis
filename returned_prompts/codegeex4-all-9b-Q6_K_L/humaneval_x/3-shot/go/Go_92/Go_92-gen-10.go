
Sure, let's tackle these problems one at a time.

#1: HasCloseElements
This function checks if any two numbers in the provided slice are closer to each other than the given threshold.

Here's the logic:

Iterate over each pair of numbers in the slice.
Calculate the absolute difference between the two numbers.
If the difference is less than the threshold, return true.
If no such pair is found, return false.

Here's the complete function:
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

#2: SeparateParenGroups
This function takes a string containing multiple groups of nested parentheses and separates them into separate strings.

Here's the logic:

Create an empty slice to store the result.
Iterate over each character in the input string.
Count the depth of parentheses using a counter.
If the character is an opening parenthesis, increment the counter and add it to the current string.
If the character is a closing parenthesis, decrement the counter and add it to the current string.
If the counter reaches zero, it means we've completed a group of parentheses. Add the current string to the result and reset the current string.
Return the result.

Here's the complete function:
```go
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth++
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth--
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

#3: TruncateNumber
This function takes a positive floating-point number and returns the decimal part of the number.

Here's the logic:

