    result := operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i+1]
        case "-":
            result -= operand[i+1]
        case "*":
            result *= operand[i+1]
        case "/":
            result /= operand[i+1]
        case "//":
            result //= operand[i+1]
        case "**":
            result **= operand[i+1]
        }
    }
    return result
}



