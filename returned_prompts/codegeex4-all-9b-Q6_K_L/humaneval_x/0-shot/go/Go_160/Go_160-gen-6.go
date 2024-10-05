import (
	"math"
	"sort"
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
	// Sort the operator and operand lists based on the order of operations
	sort.Slice(operator, func(i, j int) bool {
		ops := map[string]int{
			"+": 0,
			"-": 0,
			"*": 1,
			"/": 1,
			"//": 2,
			"**": 3,
		}
		return ops[operator[i]] < ops[operator[j]]
	})
	sort.Slice(operand, func(i, j int) bool {
		return i < j
	})

	// Evaluate the expression
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
		}
	}
	return result
}
