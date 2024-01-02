import (
    "math"
)

// Given two lists operator, and operand. The first list has basic algebra operations, and
// the second list is a list of integers. Use the two given lists to build the algebric
// expression and return the evaluation of this expression.
// 
// The basic algebra operations:
// Addition ( + )
// Subtraction ( - )
// Multiplication ( * )
// Floor division ( // )
// Exponentiation ( ** )
// 
// Example:
// operator['+', '*', '-']
// array = [2, 3, 4, 5]
// result = 2 + 3 * 4 - 5
// => result = 9
// 
// Note:
// The length of operator list is equal to the length of operand list minus one.
// Operand is a list of of non-negative integers.
// Operator list has at least one operator, and operand list has at least two operands.
func DoAlgebra(operator []string, operand []int) int {
    var i = 0
    var j = 1 // j to track the index of operand

    for _, op := range operator[i:len(operator)-2] {
        switch op {
        case "+":
            a := operand[j-1] + operand[j]
            if a > i && a < j - 1 {
                return (a)
            } else {
                j++
            }
        case "-":
            b := int(math.Pow(2, i))
            c := (b * (operand[j-1] + operand[j])) / b
            if (c < -i || c > j) && (c >= 0 && c <= i) {
                return (c)
            } else {
                j++
            }
        case "*":
            a := operand[j-1] * operand[j]
            if a > i && a < j - 2 {
                return a
            } else {
                j += 2
            }
        case "/", "//":
            div := float64(operand[j]) /