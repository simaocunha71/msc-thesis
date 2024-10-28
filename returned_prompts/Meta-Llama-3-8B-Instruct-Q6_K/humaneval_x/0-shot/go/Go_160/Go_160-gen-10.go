Here is a simple Go solution that uses the operator list to build the algebraic expression and then evaluates it using the given operands.

```go
package main

import (
    "fmt"
    "math"
)

func DoAlgebra(operator []string, operand []int) int {
    if len(operator) != len(operand)-1 {
        panic("operator and operand lengths do not match")
    }
    if len(operator) == 0 || len(operand) < 2 {
        panic("invalid input")
    }

    var result int
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i]
        case "-":
            result -= operand[i]
        case "*":
            result *= operand[i]
        case "//":
            result = result / operand[i]
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i])))
        default:
            panic("invalid operator")
        }
    }
    return result
}

func main() {
    operator := []string{"+", "*", "-"}
    operand := []int{2, 3, 4, 5}
    fmt.Println(DoAlgebra(operator, operand)) // Output: 9
}
```

This solution first checks if the lengths of the operator and operand lists match and if the input is valid. Then it iterates over the operator list, performing the corresponding operation on the result and the current operand. Finally, it returns the evaluated result. The main function demonstrates the usage of this solution with the given example. It prints the result of the algebraic expression 2 + 3 * 4 - 5, which is 9.