for i := 0; i < len(operand)-1; i++ {

B:
    switch operator[i] {
    case "+":
        result += operand[i]
    case "-":
        result -= operand[i]
