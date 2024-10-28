    i := 0
    for _, op := range operator {
        if op == "+" {
            operand[i] += operand[i + 1]
        }else if op == "-" {
            operand[i] -= operand[i + 1]
        }else if op == "*" {
            operand[i] *= operand[i + 1]
        }else if op == "/" {
            operand[i] /= operand[i + 1]
        }else if op == "//" {
            operand[i] /= operand[i + 1]
            operand[i] = int(math.Floor(float64(operand[i])))
        }else if op == "**" {
            operand[i] = int(math.Pow(float64(operand[i]), float64(operand[i + 1])))
        }
        i += 1
    }
    return operand[0]
}



