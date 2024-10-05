    result := operand[0]
    for i, op := range operator {
        if op == "+" {
            result += operand[i + 1]
        } else if op == "-" {
            result -= operand[i + 1]
        } else if op == "*" {
            result *= operand[i + 1]
        } else if op == "//" {
            result /= operand[i + 1]
        } else if op == "**" {
            result = int(math.Pow(float64(result), float64(operand[i + 1])))
        }
    }
    return result
}



