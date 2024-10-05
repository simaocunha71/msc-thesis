    result := operand[0]
    for i := 1; i < len(operand); i++ {
        switch operator[i-1] {
        case "+":
            result += operand[i]
        case "-":
            result -= operand[i]
        case "*":
            result *= operand[i]
        case "//":
            result /= operand[i]
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i])))
        default:
            panic("Invalid operator")
        }
    }
    return result
}


