    result := operand[0]
    for i := 0; i < len(operator); i++ {
        var left int
        var right int
        switch operator[i] {
        case "+":
            right = operand[i + 1]
            result += right
        case "-":
            right = operand[i + 1]
            result -= right
        case "*":
            right = operand[i + 1]
            result *= right
        case "/":
            right = operand[i + 1]
            result /= right
        case "**":
            right = operand[i + 1]
            result = int(math.Pow(float64(result), float64(right)))
        }
    }
    return result
}