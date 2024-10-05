    result := 0

    for i, op := range operator {
        switch op {
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

*/

// DoAlgebra calculates a simple arithmetic expression from given operators and operands.
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
		case "/":
			result /= operand[i]
		case "**":
			result = int(math.Pow(float64(result), float64(operand[i])))
		default:
			panic("Unknown operator: " + operator[i-1])
		}
	}

	return result
}

// DoAlgebra2 is the same function but uses a different approach to solve the problem.
func DoAlgebra2(operator []string, operand []int) int {
	result := operand[0]

	for i := 1; i < len(operand); i++ {
		switch operator[i-1] {
		case "+":
			result = result + operand[i]
		case "-":
			result = result - operand[i]
		case "*":
			result = result * operand[i]
		case "//":
			result = result / operand[i]
		case "