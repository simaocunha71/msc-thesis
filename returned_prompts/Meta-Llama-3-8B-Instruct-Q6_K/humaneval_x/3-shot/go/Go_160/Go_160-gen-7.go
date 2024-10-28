    result := operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += int64(operand[i+1])
        case "-":
            result -= int64(operand[i+1])
        case "*":
            result *= int64(operand[i+1])
        case "/":
            result /= int64(operand[i+1])
        case "//":
            result = int(result / int64(operand[i+1]))
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
        }
    }
    return result
}