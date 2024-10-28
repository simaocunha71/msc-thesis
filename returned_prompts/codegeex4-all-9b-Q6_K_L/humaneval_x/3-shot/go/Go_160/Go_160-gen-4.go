    result := operand[0]
    for i:=0; i<len(operator); i++{
        if operator[i] == "+{
            result += operand[i+1]
        }else if operator[i] == "-{
            result -= operand[i+1]
        }else if operator[i] == "*{
            result *= operand[i+1]
        }else if operator[i] == "//{
            result = result // operand[i+1]
        }else if operator[i] == "**{
            result = result ** operand[i+1]
        }
    }
    return result
}

