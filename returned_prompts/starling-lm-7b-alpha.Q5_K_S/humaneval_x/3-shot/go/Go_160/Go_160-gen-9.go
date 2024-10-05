    result := operand[0]
    for i, operator_type := range operator {
        if i == 0 {
            continue
        }
        if operator_type == "+" {
            result += operand[i]
        }else if operator_type == "-" {
            result -= operand[i]
        }else if operator_type == "*" {
            result *= operand[i]
        }else if operator_type == "//" {
            result /= operand[i]
        }else if operator_type == "**" {
            result = int(math.Pow(float64(result), float64(operand[i])))
        }
    }
    return result
}



