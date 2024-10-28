    result := operand[0]
    for i, op := range operator {
        switch op {
        case "+":
            result += operand[i + 1]
        case "-":
            result -= operand[i + 1]
        case "*":
            result *= operand[i + 1]
        case "/":
            result /= operand[i + 1]
        case "//":
            result /= int(math.Floor(float64(operand[i + 1])))
        case "**":
            result **= operand[i + 1]
        }
    }
    return result
}



