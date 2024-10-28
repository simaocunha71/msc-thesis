    for _, op := range operator {
        switch op {
        case "+":
            return operand[0] + operand[1]
        case "-":
            return operand[0] - operand[1]
        case "*":
            return operand[0] * operand[1]
        case "/":
            return operand[0] / operand[1]
        case "//":
            return operand[0] // operand[1]
        case "**":
            return math.Pow(operand[0], operand[1])
        }
    }
    return -1
}
