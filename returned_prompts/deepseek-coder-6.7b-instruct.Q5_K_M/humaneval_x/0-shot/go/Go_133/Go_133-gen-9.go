    var sum float64 = 0

    for _, num := range lst {
        // Round each element in the list to the upper int(Ceiling)
        ceil := math.Ceil(num)
        // Square each rounded element and add it to the sum
        sum += math.Pow(ceil, 2)
    }

    // Return the sum as an int
    return int(sum)

}
```

## テストケース

```go
package main

import (
    "fmt"
    "math"
    "testing"
)

func TestSumSquares(t *testing.T) {
    type test struct {
        input []float64
        expected int
    }

    tests := []test{
        {[]float64{1, 2, 3}, 14},
        {[]float64{1, 4, 9}, 98},
        {[]float64{1, 3, 5, 7}, 84},
        {[]float64{1.4, 4.2, 0}, 29},
        {[]float64{-2.4, 1, 1}, 6},
    }

    for _, test := range tests {
        got := SumSquares(test.input)
        if got != test.expected {
            t.Errorf("SumSquares(%v) = %v; want %v", test.input, got, test.expected)
        }
    }
}

func main() {
    fmt.Println(SumSquares([]float64{1, 2, 3})) // 14
    fmt.Println(SumSquares([]float64{1, 4, 9})) // 98
    fmt.Println(SumSquares([]float64{1, 3, 5, 7})) // 84
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0})) // 29
    fmt