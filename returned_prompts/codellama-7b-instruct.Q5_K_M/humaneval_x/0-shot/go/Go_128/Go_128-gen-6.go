
package main

import (
    "fmt"
    "math"
)

func main() {
    var testCases = []struct {
        input    []int
        expected interface{}
    }{
        {
            input:    []int{},
            expected: nil,
        },
        {
            input:    []int{0, 1},
            expected: 0,
        },
        {
            input:    []int{1, 2, 2, -4},
            expected: -9,
        },
    }
    for _, tc := range testCases {
        actual := ProdSigns(tc.input)
        fmt.Printf("Expected: %v, Actual: %v\n", tc.expected, actual)
    }
}

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    product, sign := 1, 1
    for _, num := range arr {
        sign = 1
        if num < 0 {
            sign = -1
        }
        product *= sign
        num *= sign
    }
    var sum int
    for _, num := range arr {
        sum += int(math.Abs(float64(num)))
    }
    return sum * product
}
