    var result int

    i := 0
    for len(operator) > 1 {
        result += eval(operator[i], operand[i], operand[i+1])
        i += 2
    }
    return result
}

func eval(op string, a, b int) int {
    switch op {
    case "+":
        return a + b
    case "-":
        return a - b
    case "*":
        return a * b
    case "//":
        return a / b
    case "**":
        return int(math.Pow(float64(a), float64(b)))
    }
    return 0
}
























// The length of operator list is equal to the length of operand list minus one.
// Operand is a list of of non-negative integers.
// Operator list has at least one operator, and operand list has at least two operands.
// Given two lists operator, and operand. The first list has basic algebra operations, and
// the second list is a list of integers. Use the two given lists to build the algebric
// expression and return the evaluation of this expression.
// 
// The basic algebra operations:
// Addition (+)
// Subtraction (-)
// Multiplication (*)
// Floor division (//)
// Exponentiation (**
// 
// Example:
// operator = ['+', '*', '-']
// array = [2, 3, 4, 5]
// result = 2 + 3 * 4 - 5
// => result = 9
func DoAlgebra(operator []string, operand []int) int {
    result := 0

    for i := 0; i < len(operator); i++ {
        result += eval(operator[i], operand[i], operand[i+1])
        i += 1
    }

    return result
}

func eval(op string, a, b int) int {
    switch op {
    case "+":
        return a + b
    case "-":
        return a - b
   