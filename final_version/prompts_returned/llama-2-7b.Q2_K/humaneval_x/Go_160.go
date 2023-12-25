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
    // Get the length of both lists.
    if len(operator[0:]) < len(operand)-1 || len(operator)-1 <= 0 {
        return math.MaxInt64
    } else {
        var ans = 0
        
        for i := range operator {
            for j := range operand[len(operator):] - 1 {
                if i == len(operator) - 1 ||
                   !IsAlgebraic(ans, operator[i]) && !IsAlgebraic(ans, operand[j]){
                    ans = 0
                } else {
                    ans += (ans * math.Pow(2.0, i)) % math.MaxInt64 // Evaluate the expression.
                }
            }
        }
        
        return ans 
}