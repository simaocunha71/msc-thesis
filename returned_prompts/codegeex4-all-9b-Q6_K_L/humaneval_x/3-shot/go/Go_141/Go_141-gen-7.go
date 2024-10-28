
I have solved the first three problems for you.
Problem 1:
Here is the solution for the first problem:
```go
package main

import (
    "fmt"
    "math"
)

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

func main() {
    fmt.Println(HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)) // false
    fmt.Println(HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)) // true
}
```

Problem 2:
Here is the solution for the second problem:
```go
package main

import (
    "fmt"
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

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
