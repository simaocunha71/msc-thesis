result := operand[0]
i := 1

for _, op := range operator {
    switch op {
    case "+":
        result += operand[i]
    case "-":
        result -= operand[i]
    case "*":
        result *= operand[i]
    case "//":
        result /= operand[i]
    case "**":
        result = int(math.Pow(float64(result), float64(operand[i])))
    default:
        fmt.Printf("Unknown operation %s\n", op)
        return -1
    }
    i++
}
return result


A: Here is a simple solution using a stack. The solution is based on the fact that a stack follows the LIFO (Last In First Out) principle. This means that the last element added to the stack will be the first one to be removed. 

In this solution, we use a stack to store the operands and apply the operators to the last two operands in the stack.

```go
package main

import (
	"fmt"
	"strconv"
)

// Stack structure
type Stack struct {
	Items []int
}

// Push function to add an element to the stack
func (s *Stack) Push(i int) {
	s.Items = append(s.Items, i)
}

// Pop function to remove an element from the stack
func (s *Stack) Pop() int {
	last := len(s