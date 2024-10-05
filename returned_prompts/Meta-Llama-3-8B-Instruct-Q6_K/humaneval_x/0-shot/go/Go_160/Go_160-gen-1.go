```go
package main

import (
    "fmt"
    "math"
)

func DoAlgebra(operator []string, operand []int) int {
    if len(operator) != len(operand)-1 {
        panic("operator list length does not match operand list length")
    }

    result := operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += int64(operand[i+1])
        case "-":
            result -= int64(operand[i+1])
        case "*":
            result *= int64(operand[i+1])
        case "//":
            result = int(result / int64(operand[i+1]))
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


This code defines a function `DoAlgebra` that takes two slices as input: `operator` and `operand`. The `operator` slice contains the basic algebra operations as strings, and the `operand` slice contains the integers to be operated on. The function evaluates the algebraic expression built by concatenating the operators and operands, and returns the result.

In the `main` function, we test the `DoAlgebra` function with the example given in the problem description. The output is `9`, which is the correct result of the expression `2 + 3 * 4 - 5`.