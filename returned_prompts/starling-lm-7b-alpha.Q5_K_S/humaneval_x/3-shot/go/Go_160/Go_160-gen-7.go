    result := operand[0]
    for i:= 0; i < len(operator); i++ {
        if operator[i] == "+" {
            result = strconv.Itoa(result) + strconv.Itoa(operand[i+1])
        }else if operator[i] == "*" {
            result = strconv.Itoa(result*operand[i+1])
        }else if operator[i] == "-" {
            result = strconv.Itoa(result - operand[i+1])
        }else if operator[i] == "//" {
            result = strconv.Itoa(result / operand[i+1])
        }else if operator[i] == "**" {
            result = strconv.Itoa(math.Pow(float64(result),float64(operand[i+1])))
        }
    }
    return result
}



