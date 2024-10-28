
For the first question, you need to check if the current number is close to any of the previously checked numbers. Here's how you can do it:
```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}
```
This code will check every pair of numbers in the list and return true if any two numbers are closer than the given threshold.
For the second question, you need to iterate through the input string and keep track of the current depth of nested parentheses. Here's how you can do it:
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
This code will iterate through the input string and separate the groups of parentheses into separate strings.
For the third question, you need to truncate the number by taking the modulus of the number and 1. Here's how you can do it:
```go
func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}
```
This code will return the decimal part of the number.
For the fourth question, you need to split the input string into words, sort the characters in each word,