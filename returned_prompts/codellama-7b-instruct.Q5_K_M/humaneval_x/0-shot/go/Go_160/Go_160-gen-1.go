	for i, op := range operator {
		switch op {
		case "+":
			operand[i+1] += operand[i]
			operand[i] = 0
		case "-":
			operand[i+1] -= operand[i]
			operand[i] = 0
		case "*":
			operand[i+1] *= operand[i]
			operand[i] = 0
		case "/":
			operand[i+1] = operand[i+1] / operand[i]
			operand[i] = 0
		case "**":
			operand[i+1] = math.Pow(operand[i+1], operand[i])
			operand[i] = 0
		}
	}

	return operand[len(operand)-1]
}
