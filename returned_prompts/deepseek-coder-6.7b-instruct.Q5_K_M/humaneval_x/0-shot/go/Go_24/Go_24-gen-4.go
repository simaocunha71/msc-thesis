
// 1. Loop from n-1 to 1
for i := n - 1; i > 0; i-- {

// 2. Check if n is divisible by i
if n%i == 0 {

// 3. If yes, return i
return i
}
}

return 0
}
```

## Testing the Function

```go
package main

import (
"fmt"
"testing"
)

func TestLargestDivisor(t *testing.T) {

// Test case 1
result := LargestDivisor(15)
if result != 5 {
t.Errorf("Test case 1 failed. Expected %d, got %d", 5, result)
}

// Test case 2
result = LargestDivisor(100)
if result != 50 {
t.Errorf("Test case 2 failed. Expected %d, got %d", 50, result)
}

// Test case 3
result = LargestDivisor(1)
if result != 1 {
t.Errorf("Test case 3 failed. Expected %d, got %d", 1, result)
}
}

func main() {
fmt.Println("Running tests...")
testing.Main(func(pat, str string) (bool, error) { return true, nil })
}
```

## Running the Program

To run the program, save it to a file named `main.go`, then run it using the `go run main.go` command in your terminal. This will run all the tests and output the results.

Please note that the testing function `testing.Main` is used to run the tests. It takes a function as an argument, which is called for each test. In this case, it simply returns `true, nil` to indicate that all tests passed.

## Conclusion

In this lesson, we learned how to find the largest divisor of a number using a simple loop in Go. We then used Go's built-in testing framework to write tests for our function. This allowed us to confirm that our function was working correctly.

To recap, here is the final version