    // Add your code here
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}

Please write the unit tests for SumToN function.

```go
func TestSumToN(t *testing.T) {
    // Add your test cases here
    if SumToN(1) != 1 {
        t.Errorf("SumToN(1) = %d, want %d", SumToN(1), 1)
    }
    if SumToN(5) != 15 {
        t.Errorf("SumToN(5) = %d, want %d", SumToN(5), 15)
    }
    if SumToN(10) != 55 {
        t.Errorf("SumToN(10) = %d, want %d", SumToN(10), 55)
    }
    if SumToN(30) != 465 {
        t.Errorf("SumToN(30) = %d, want %d", SumToN(30), 465)
    }
    if SumToN(100) != 5050 {
        t.Errorf("SumToN(100) = %d, want %d", SumToN(100), 5050)
}
```

The `SumToN` function calculates the sum of all numbers from 1 to `n`. You can write unit tests for this function to ensure it is working correctly. The `testing` package in Go provides a simple way to write unit tests. You can write test cases for different inputs and expected outputs. If the actual output does not match the expected output, the test will fail and the error message will be printed. 

In this example, we have written test cases for inputs 1, 5, 10, 30, and 100. For each test case, we call the `SumToN` function with the given input and compare the result with the expected output. If the result does not match the expected output, the test will fail and the error message will be printed. 

You can run the test using the command `go test` in the terminal. If all tests pass, you will see a message saying "ok". If any test fails, you will see an error message indicating which test failed and why. 

Here is the complete code:

```go
package main

import (
    "testing"
)

