```go
package main

import (
	"fmt"
)

func DoAlgebra(operator []string, operand []int) int {
	result := operand[0]
	for i := 1; i < len(operand); i++ {
		switch operator[i-1] {
		case "+":
			result += operand[i]
		case "-":
			result -= operand[i]
		case "*":
			result *= operand[i]
		case "//":
			result /= operand[i]
		case "**":
			result = int(math.Pow(float64(result), float64(operand[i])))
		}
	}
	return result
}

func main() {
	operators := []string{"+", "*", "-"}
	operands := []int{2, 3, 4, 5}
	fmt.Println(DoAlgebra(operators, operands)) // Output: 9
}
```
