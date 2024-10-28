Here is the solution:
```go
import (
    "math"
)

func DoAlgebra(operator []string, operand []int) int {
    result := operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i + 1]
        case "-":
            result -= operand[i + 1]
        case "*":
            result *= operand[i + 1]
        case "/":
            result = int(math.Floor(float64(result) / float64(operand[i + 1])))
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i + 1])))
        }
    }
    return result
}
```
Explanation:

*   We initialize the result with the first element of the operand list.
*   We iterate through the operator list and corresponding operand list.
*   For each operator, we perform the corresponding operation on the result and the operand.
*   We use a switch statement to handle the different operators.
*   For the division operator, we use the math.Floor function to perform floor division.
*   For the exponentiation operator, we use the math.Pow function to calculate the power.
*   Finally, we return the final result.

Note: This implementation assumes that the operator list has at least one operator and the operand list has at least two operands. If the input does not satisfy these conditions, the function may panic or return incorrect results. You may want to add error handling to handle such cases.