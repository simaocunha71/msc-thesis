    for _, op := range operator {
        switch op {
        case "+":
            result += operand[i+1]
            i++
        case "-":
            result -= operand[i+1]
            i++
        case "*":
            result *= operand[i+1]
            i++
        case "//":
            result /= operand[i+1]
            i++
        case "**":
            result = math.Pow(float64(result), float64(operand[i+1]))
            i++
        default:
            fmt.Printf("Unknown operator %s\n", op)
            return 0
        }
    }
    return result
}

func main() {
    operator := []string{"+", "*", "-"}
    operand := []int{2, 3, 4, 5}
    fmt.Println(DoAlgebra(operator, operand))  // Should print 9
}


A: You need to initialize i to 0 and result to the first operand before the loop. 
Also, you should increment i only after the operation, as per the problem statement.
Here is the corrected code:

```go
package main

import (
    "fmt"
    "math"
)

func DoAlgebra(operator []string, operand []int) int {
    result := operand[0]
    i := 0

    for _, op := range operator {
        switch op {
        case "+":
            result += operand[i+1]
            i++
        case "-":
            result -= operand[i+1]
            i++
        case "*":
            result *= operand[i+1]
            i++
        case "//":
            result /= operand[i+1]
            i++
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
            i++
        default:
            fmt.Printf("Unknown operator %s\n", op)
            return 0