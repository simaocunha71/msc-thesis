```go
func DoAlgebra(operator []string, operand []int) int {
    // Initialize the result with the first operand
    result := operand[0]

    // Iterate through the operator and operand lists
    for i := 0; i < len(operator); i++ {
        // Perform the operation based on the current operator
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

    // Return the final result
    return result
}
```

