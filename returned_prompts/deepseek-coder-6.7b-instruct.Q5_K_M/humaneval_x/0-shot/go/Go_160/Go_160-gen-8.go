    result := operand[0]

    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i+1]
        case "-":
            result -= operand[i+1]
        case "*":
            result *= operand[i+1]
        case "//":
            result /= operand[i+1]
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
        default:
            break A
        }
    }

    return result
}

This is a simple solution to your problem in Go language.
The function "DoAlgebra" accepts two lists, one for the operators and one for the operands. It calculates the result by iterating over the operators and applying them sequentially to the operands. If the operator is not recognized, it breaks the loop and returns the current result.
*/

package main

import (
	"fmt"
)

func DoAlgebra(operator []string, operand []int) int {
	result := operand[0]

	for i := 0; i < len(operator); i++ {
		switch operator[i] {
		case "+":
			result += operand[i+1]
		case "-":
			result -= operand[i+1]
		case "*":
			result *= operand[i+1]
		case "//":
			result /= operand[i+1]
		case "**":
			result = int(math.Pow(float64(result), float64(operand[i+1])))
		default:
			break
		}
	}

	return result
}

func main() {
	operators := []string{"+", "*", "-"}
	operands := []int{2, 3, 4, 5}

	result := DoAlgebra(operators, operands)

	fmt.Println("Result:", result)
}

/*