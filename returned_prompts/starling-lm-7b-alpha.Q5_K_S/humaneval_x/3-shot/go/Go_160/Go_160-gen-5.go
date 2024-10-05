    result := operand[0]
    for i:=1;i<len(operator);i+=2{
        if operator[i] == "+"{
            result = strconv.Itoa(result + operand[i+1])
        }else if operator[i] == "-"{
            result = strconv.Itoa(result - operand[i+1])
        }else if operator[i] == "*"{
            result = strconv.Itoa(result * operand[i+1])
        }else if operator[i] == "//"{
            result = strconv.Itoa(result / operand[i+1])
        }else if operator[i] == "**"{
            result = strconv.Itoa(result * operand[i+1])
        }
    }
    return result
}



