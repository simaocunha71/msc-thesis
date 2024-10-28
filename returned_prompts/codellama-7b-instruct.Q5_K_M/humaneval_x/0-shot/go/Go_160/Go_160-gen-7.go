    for i := len(operator) - 1; i >= 0; i-- {
        switch operator[i] {
        case "+":
            operand[i+1] += operand[i]
        case "-":
            operand[i+1] -= operand[i]
        case "*":
            operand[i+1] *= operand[i]
        case "/":
            operand[i+1] /= operand[i]
        case "//":
            operand[i+1] = int(math.Floor(float64(operand[i+1]) / float64(operand[i])))
        case "**":
            operand[i+1] = int(math.Pow(float64(operand[i+1]), float64(operand[i])))
        default:
            continue A
        }
    }

    return operand[len(operand)-1]
}