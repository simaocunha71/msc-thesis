
You can use the testing package from Go.
Here's an example of how to write a test for your first function:
```go
package main

import (
    "math"
    "testing"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}

func TestHasCloseElements(t *testing.T) {
    // Test case 1
    numbers1 := []float64{1.0, 2.0, 3.0}
    threshold1 := 0.5
    expected1 := false
    result1 := HasCloseElements(numbers1, threshold1)
    if result1 != expected1 {
        t.Errorf("Expected %v, but got %v", expected1, result1)
    }

    // Test case 2
    numbers2 := []float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}
    threshold2 := 0.3
    expected2 := true
    result2 := HasCloseElements(numbers2, threshold2)
    if result2 != expected2 {
        t.Errorf("Expected %v, but got %v", expected2, result2)
    }
}
```
You can then run the tests using the `go test` command. If any of the test cases fail, the error message will be printed out.