    if IsPrime(n){
        return x
    }
    return y
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

I am new to Go and I am trying to run these codes. I saved them in a file named 'main.go' and tried to run them using 'go run main.go' command in my terminal. But I am getting the following error:

main.go:2:2: syntax error: non-declaration statement outside function body
main.go:10:2: syntax error: non-declaration statement outside function body

I am not sure what I am doing wrong. Any help is appreciated.

A: The error you are seeing is because you've written the code outside of any function. Functions in Go are the basic unit of code organization, and your code seems to be missing function definitions.
Here's your code with the appropriate function definitions added:
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
            current_string = append(current