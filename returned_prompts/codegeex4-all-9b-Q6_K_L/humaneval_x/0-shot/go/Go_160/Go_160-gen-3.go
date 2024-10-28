```go
import (
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
// operator['+', '*', '-']
// array = [2, 3, 4, 5]
// result = 2 + 3 * 4 - 5
// => result = 9
// 
// Note:
// The length of operator list is equal to the length of operand list minus one.
// Operand is a list of of non-negative integers.
// Operator list has at least one operator, and operand list has at least two operands.
func DoAlgebra(operator []string, operand []int) int {
    // Initialize the result with the first operand
    result := operand[0]

    // Iterate through the operator and operand lists
    for i := 0; i < len(operator); i++ {
        // Get the current operator and operand
        op := operator[i]
        val := operand[i+1]

        // Perform the operation and update the result
        switch op {
        case "+":
            result += val
        case "-":
            result -= val
        case "*":
            result *= val
        case "//":
            result = result / val
        case "**":
            result = int(math.Pow(float64(result), float64(val)))
        }
    }

    // Return the result
    return result
}
```
