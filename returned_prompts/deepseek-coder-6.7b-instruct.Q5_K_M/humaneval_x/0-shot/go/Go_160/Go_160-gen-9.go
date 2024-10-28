    for i := 0; i < len(operator); i++ {
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

*/

package main

import (
	"fmt"
	"math"
)

func DoAlgebra(operator []string, operand []int) int {

	for i := 0; i < len(operator); i++ {
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

func main() {
	operators := []string{"+", "*", "-"}
	operands := []int{2, 3, 4, 5}
	result := DoAlgebra(operators, operands)
	f