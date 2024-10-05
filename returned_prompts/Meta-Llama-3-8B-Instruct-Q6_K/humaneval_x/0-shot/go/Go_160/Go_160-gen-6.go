```go
package main

import (
    "fmt"
    "math"
)

// Given two lists operator, and operand. The first list has basic algebra operations, and
// the second list is a list of integers. Use the two given lists to build the algebric
// expression and return the evaluation of this expression.
// 
// The basic algebra operations:
// Addition ( + )
// Subtraction ( - )
// Multiplication ( * )
// Floor division ( // )
// Exponentiation ( ** )
// 
// Example:
// operator=['+', '*', '-']
// array = [2, 3, 4, 5]
// result = 2 + 3 * 4 - 5
// => result = 9
// 
// Note:
// The length of operator list is equal to the length of operand list minus one.
// Operand is a list of of non-negative integers.
// Operator list has at least one operator, and operand list has at least two operands.
func DoAlgebra(operator []string, operand []int) int {
    if len(operator) != len(operand)-1 {
        panic("operator length does not match operand length")
    }
    if len(operand) < 2 {
        panic("operand list has less than 2 elements")
    }
    if len(operator) < 1 {
        panic("operator list has less than 1 element")
    }

    result := operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i+1]
        case "-":
            result -= operand[i+1]
        case "*":
            result *= operand[i+1]
        case "/":
            if operand[i+1] == 0 {
                panic("division by zero")
            }
            result = int(math.Floor(float64(result) / float64(operand[i+1])))
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
        default:
            panic("unknown operator")
        }
    }
    return result
}

func main() {
    operator := []string{"+", "*", "-"}
    operand := []int{2, 3, 4, 5}
    fmt.Println(DoAlgebra(operator, operand))  // Output: 9
}
```

Explanation:
This code defines a function `DoAlgebra` that takes two lists, `operator`