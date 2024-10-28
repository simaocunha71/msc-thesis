    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            operand[i] = operand[i] + operand[i+1]
            operand = append(operand[:i], operand[i+1:]...)
            i--
        case "-":
            operand[i] = operand[i] - operand[i+1]
            operand = append(operand[:i], operand[i+1:]...)
            i--
        case "*":
            operand[i] = operand[i] * operand[i+1]
            operand = append(operand[:i], operand[i+1:]...)
            i--
        case "/":
            operand[i] = operand[i] / operand[i+1]
            operand = append(operand[:i], operand[i+1:]...)
            i--
        case "**":
            operand[i] = math.Pow(operand[i], operand[i+1])
            operand = append(operand[:i], operand[i+1:]...)
            i--
        default:
            continue A
        }
    }

    return operand[0]
}
