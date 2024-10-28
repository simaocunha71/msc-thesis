    result := 0
    for i := 0; i < len(operand); i++ {
        switch operator[i] {
        case "+":
            result += operand[i]
        case "-":
            result -= operand[i]
        case "*":
            result *= operand[i]
        case "/":
            result /= operand[i]
        case "//":
            result //= operand[i]
        case "**":
            result **= operand[i]
        }
    }
    return result
}



