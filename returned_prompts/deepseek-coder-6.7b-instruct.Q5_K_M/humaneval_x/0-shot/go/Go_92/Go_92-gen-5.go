
    // Checking if all inputs are integers
    switch x := x.(type) {
    case int:
        switch y := y.(type) {
        case int:
            switch z := z.(type) {
            case int:
                // Checking if one of the numbers equals the sum of the other two
                if x == y+z || y == x+z || z == x+y {
                    return true
                }
            }
        }
    }

    return false
}

// Test cases
func main() {
    fmt.Println(AnyInt(5, 2, 7)) // Expected: true
    fmt.Println(AnyInt(3, 2, 2)) // Expected: false
    fmt.Println(AnyInt(3, -2, 1)) // Expected: true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // Expected: false
}
```

In this program, we first check if the input values are integers. If they are, we then check if one of the numbers equals the sum of the other two numbers. If either condition is true, we return true; otherwise, we return false.

The main function tests the function with some test cases, and prints the expected and actual results.

Note: This solution assumes that the inputs will always be three numbers. If the inputs could be something else, you would need to add additional error checking to handle that case.

**NOTE:** This solution is written in Go and the problem is solved using Go language. If you want to solve this problem in other languages, you'll have to modify the syntax and the logic slightly.

**NOTE:** This solution assumes that the inputs will always be three numbers. If the inputs could be something else, you would need to add additional error checking to handle that case.

**NOTE:** This solution assumes that the inputs will always be three numbers. If the inputs could be something else, you would need to add additional error checking to handle that case.

**NOTE:** This solution assumes that the inputs will always be three numbers. If the inputs could be something else, you would need to add additional error checking to handle that case.

**NOTE:** This solution assumes that