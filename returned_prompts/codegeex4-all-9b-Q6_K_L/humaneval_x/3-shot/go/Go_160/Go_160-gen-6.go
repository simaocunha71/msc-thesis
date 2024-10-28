    result := operand[0]

    for i, o := range operator {
        switch o {
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



