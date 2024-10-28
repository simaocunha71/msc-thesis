    for i, v := range operator {
        switch v {
        case "+":
            operand[i+1] += operand[i]
        case "-":
            operand[i+1] -= operand[i]
        case "*":
            operand[i+1] *= operand[i]
        case "/":
            operand[i+1] /= operand[i]
        case "%":
            operand[i+1] %= operand[i]
        case "**":
            operand[i+1] **= operand[i]
        case "//":
            operand[i+1] //= operand[i]
        case "|":
            operand[i+1] |= operand[i]
        case "&":
            operand[i+1] &= operand[i]
        case "<<":
            operand[i+1] <<= operand[i]
        case ">>":
            operand[i+1] >>= operand[i]
        case "^":
            operand[i+1] ^= operand[i]
        }
    }

    return operand[len(operand)-1]
}

// Given a string s representing an expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
// 
// Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
func BasicCalculator(s string) int {

    stack := []int{}
    operator := ""
    operand := 0

    for _, v := range s {
        switch v {
        case ' ':
            continue
        case '+':
            operator = "+"
            stack = append(stack, operand)
            operand = 0
        case '-':
            operator = "-"
            stack = append(stack, operand)
            operand = 0
        case '*':
            operator = "*"
            stack = append(stack, operand)
            operand = 0
        case '/':
            operator = "/"
            stack = append(stack,