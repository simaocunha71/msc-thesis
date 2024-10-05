

A: It seems like you've misunderstood the problem. If you want to evaluate an expression given in infix notation (like "2 + 3 * 4 - 5"), you should parse it into postfix notation (like "2 3 4 * + 5 -"), then evaluate it.

In Python, you can use the built-in `eval` function to evaluate a string as a Python expression. But if you want to implement it yourself, you need to parse the infix notation into postfix notation, then evaluate it.

Here is a basic implementation of this in Go:

```go
package main

import (
	"fmt"
	"strconv"
)

func EvaluateExpression(expression string) int {
	operators := []string{}
	operands := []int{}
	number := 0
	negative := false
	for _, char := range expression {
		switch char {
		case '+', '-', '*', '/':
			if negative {
				number = -number
				negative = false
			}
			operands = append(operands, number)
			number = 0
			operators = append(operators, string(char))
		case ' ':
			if negative {
				number = -number
				