    result := 0
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
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
        }
    }
    return result
}



