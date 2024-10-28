```go
func DoAlgebra(operator []string, operand []int) int {
    var result int = operand[0]
    for i := 0; i < len(operator); i++ {
        switch operator[i] {
        case "+":
            result += operand[i+1]
        case "-":
            result -= operand[i+1]
        case "*":
            result *= operand[i+1]
        case "//":
            result = result / operand[i+1]
        case "**":
            result = int(math.Pow(float64(result), float64(operand[i+1])))
        }
    }
    return result
}
```