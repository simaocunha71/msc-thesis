    result := 0
    for index, value := range operand {
        if index == 0 {
            result = value
        } else {
            switch operator[index - 1] {
            case "+":
                result += value
            case "-":
                result -= value
            case "*":
                result *= value
            case "/":
                result /= value
            case "%":
                result %= value
            case "**":
                result **= value
            }
        }
    }
    return result
}



