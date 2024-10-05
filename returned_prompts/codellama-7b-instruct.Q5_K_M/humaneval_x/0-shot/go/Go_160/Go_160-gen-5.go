    for _, op := range operator {

        switch op {
        case "+":
            operand[0] = operand[0] + operand[1]
            operand = operand[2:]
            continue A
        case "-":
            operand[0] = operand[0] - operand[1]
            operand = operand[2:]
            continue A
        case "*":
            operand[0] = operand[0] * operand[1]
            operand = operand[2:]
            continue A
        case "//":
            operand[0] = operand[0] / operand[1]
            operand = operand[2:]
            continue A
        case "**":
            operand[0] = int(math.Pow(float64(operand[0]), float64(operand[1])))
            operand = operand[2:]
            continue A
        }
    }

    return operand[0]
}
