    for i, j := 0, 0; i < len(operator) && j < len(operand); {
        switch operator[i] {
        case "+":
            operand[j] += operand[j+1]
            j += 2
        case "-":
            operand[j] -= operand[j+1]
            j += 2
        case "*":
            operand[j] *= operand[j+1]
            j += 2
        case "/":
            operand[j] /= operand[j+1]
            j += 2
        case "**":
            operand[j] = int(math.Pow(float64(operand[j]), float64(operand[j+1])))
            j += 2
        }
        i++
    }
    return operand[0]
}
