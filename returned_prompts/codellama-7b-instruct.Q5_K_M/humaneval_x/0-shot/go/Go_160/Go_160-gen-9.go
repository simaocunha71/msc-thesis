    for i := 0; i < len(operand); i++ {
        switch operator[i] {
            case "+":
                operand[i] = operand[i] + operand[i+1]
                break A
            case "-":
                operand[i] = operand[i] - operand[i+1]
                break A
            case "*":
                operand[i] = operand[i] * operand[i+1]
                break A
            case "/":
                operand[i] = operand[i] / operand[i+1]
                break A
            case "%":
                operand[i] = operand[i] % operand[i+1]
                break A
            case "**":
                operand[i] = math.Pow(operand[i], operand[i+1])
                break A
            case "//":
                operand[i] = math.Floor(math.Log(operand[i])/math.Log(operand[i+1]))
                break A
            default:
                operand[i] = operand[i]
        }
    }

    return operand[0]
}