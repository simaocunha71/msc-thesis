    stack := make([]int, 0)
    i:=0
    for _,op := range operator{
        if op == "+" {
            stack = append(stack, operand[i]+operand[i+1])
        }else if op == "-" {
            stack = append(stack, operand[i]-operand[i+1])
        }else if op == "*" {
            stack = append(stack, operand[i]*operand[i+1])
        }else if op == "//" {
            stack = append(stack, operand[i]/operand[i+1])
        }else if op == "**" {
            stack = append(stack, int(math.Pow(float64(operand[i]), float64(operand[i+1]))) )
        }
        i++
    }
    return stack[0]
}



