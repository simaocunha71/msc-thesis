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
            continue A
        }
    }

    return result
}

*/

// DoAlgebra function will calculate the result of the given algebra expression.
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
		default:
			continue
		}
	}

	return result
}

// DoAlgebraWithMap function will calculate the result of the given algebra expression.
func DoAlgebraWithMap(operator []string, operand []int) int {
	result := operand[0]
	op := map[string]func(int, int) int{
		"+": func(a, b int) int { return a + b },
		"-": func(a, b int) int { return a - b },
		"*": func(a, b int) int { return a * b },
		"//": func(a, b int) int {
			if b != 0 {
				return a / b
			}
			return 0
		},
		"**": func(