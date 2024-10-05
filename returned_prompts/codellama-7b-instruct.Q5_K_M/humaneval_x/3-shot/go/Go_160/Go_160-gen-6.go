    var result int = 0

    for i := 0; i < len(operator); i++ {
        var op string = operator[i]
        var num1 int = operand[i]
        var num2 int = operand[i+1]

        if op == "+" {
            result = num1 + num2
        }else if op == "-"{
            result = num1 - num2
        }else if op == "*" {
            result = num1 * num2
        }else if op == "//" {
            result = num1 // num2
        }else if op == "**" {
            result = int(math.Pow(float64(num1), float64(num2)))
        }
    }
    return result
}





