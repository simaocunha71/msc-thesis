    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            operand[i+1] += operand[i]
        case "-":
            operand[i+1] -= operand[i]
        case "*":
            operand[i+1] *= operand[i]
        case "/":
            operand[i+1] /= operand[i]
        case "%":
            operand[i+1] %= operand[i]
        case "**":
            operand[i+1] **= operand[i]
        case "//":
            operand[i+1] = int(math.Floor(float64(operand[i+1]) / float64(operand[i])))
        }
        if operand[i+1] < 0 {
            continue A
        }
    }
    return operand[len(operator)]
}

