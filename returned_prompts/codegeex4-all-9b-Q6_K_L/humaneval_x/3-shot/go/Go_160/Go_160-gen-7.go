    result := operand[0]
    for i, op := range operator {
        switch op {
        case "+":
            result += operand[i+1]
        case "-":
            result -= operand[i+1]
        case "*":
            result *= operand[i+1]
        case "//":
            result = result / operand[i+1]
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
        }
    }
    return result
}

