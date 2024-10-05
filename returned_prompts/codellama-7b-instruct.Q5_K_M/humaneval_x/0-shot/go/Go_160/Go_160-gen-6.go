	// first, I have to make sure that the length of the operator list is correct.
	if len(operator) != len(operand)-1 {
		return -1
	}

	// Now I have to make sure that all of the operand are non-negative integers.
	for _, v := range operand {
		if v < 0 {
			return -1
		}
	}

	// Now I can proceed and start building my expression.
	// I will make an expression that is composed of the operands and the operations.
	// The order of the operands and the operations is the same as the order of the
	// operator and operand list.

	// So first, I start with the first operand.
	result := operand[0]

	// Then I move on to the second operand.
	for i := 1; i < len(operand); i++ {
		// I use the operator list to get the operator.
		operator_value := operator[i-1]
		operand_value := operand[i]

		switch operator_value {
		case "+":
			result = result + operand_value
		case "-":
			result = result - operand_value
		case "*":
			result = result * operand_value
		case "/":
			result = result / operand_value
		case "%":
			result = result % operand_value
		case "**":
			result = math.Pow(result, operand_value)
		default:
			return -1
		}
	}

	return result
}
