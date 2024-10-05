    result := operand[0]
    for i, op := range operator {
        if op == "+" {
            result = strconv.Itoa(result) + strconv.Itoa(operand[i + 1])
        }else if op == "*" {
            result = strconv.Itoa(result * operand[i + 1])
        }else if op == "-" {
            result = strconv.Itoa(result - operand[i + 1])
        }else if op == "//" {
            result = strconv.Itoa(result / operand[i + 1])
        }else if op == "**" {
            result = strconv.Itoa(math.Pow(float64(result), float64(operand[i + 1])))
        }
    }
    return strconv.Atoi(result)
}



