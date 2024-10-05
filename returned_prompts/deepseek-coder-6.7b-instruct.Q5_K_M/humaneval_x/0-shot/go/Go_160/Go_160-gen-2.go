    for i := 0; i < len(operand) - 1; i++ {
        switch operator[i] {
        case "+":
            operand[i+1] = operand[i] + operand[i+1]
        case "-":
            operand[i+1] = operand[i] - operand[i+1]
        case "*":
            operand[i+1] = operand[i] * operand[i+1]
        case "/":
            operand[i+1] = operand[i] / operand[i+1]
        case "**":
            operand[i+1] = int(math.Pow(float64(operand[i]), float64(operand[i+1])))
        }
    }
    return operand[len(operand)-1]
}

The above code is a simple solution to the problem. It iterates through the operator array and applies the corresponding operation on the corresponding elements of the operand array.

It starts from the first element of the operand array and applies the first operator to the first two operands. After that, it replaces the second operand with the result and applies the next operator to the new first and second operands, and so on. This continues until the end of the operator array. The last remaining operand is the result of the whole expression.

Please note that the "/" operator is integer division. It means that the result of the division is an integer, and the fractional part is discarded.
The "**" operator is exponentiation. It means that the first operand is raised to the power of the second operand.

Also, please note that the "**" operator can lead to very large numbers, so you might want to handle such cases depending on your requirements.
*/
package main

import (
	"fmt"
)

func main() {
	operators := []string{"+", "*", "-"}
	operands := []int{2, 3, 4, 5}
	fmt.Println(DoAlgebra(operators, operands)) // Output: 9
}

func DoAlgebra(operator []string, operand