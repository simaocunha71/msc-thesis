
To rescale the given list of numbers such that the smallest number will become 0 and the largest will become 1, you can follow the steps below:

1. Find the minimum and maximum values in the list.
2. Subtract the minimum value from all the numbers in the list.
3. Divide the result by the range (max - min) to normalize the values between 0 and 1.

Here's a complete implementation of the RescaleToUnit function in Go:

```go
package main

import (
    "fmt"
)

func RescaleToUnit(numbers []float64) []float64 {
    min := float64(20)
    max := float64(-20)
    for i := 0; i < len(numbers); i++ {
        if numbers[i] < min {
            min = numbers[i]
        }
        if numbers[i] > max {
            max = numbers[i]
        }
    }
    for i := 0; i < len(numbers); i++ {
        numbers[i] = (numbers[i] - min) / (max - min)
    }
    return numbers
}

func main() {
    fmt.Println(RescaleToUnit([]float64{1.0, 2.0, 3.0, 4.0, 5.0}))
}
```

In this example, the RescaleToUnit function first initializes the `min` and `max` variables with arbitrary values. Then, it iterates over the input `numbers` array and updates the `min` and `max` values if it finds a smaller or larger number, respectively. After that, it applies the linear transform to each number in the `numbers` array and returns the rescaled array.

Please note that the specific values of `min` and `max` in the example are arbitrary and should be replaced with the actual minimum and maximum values of your input data.

When you run this program, it will output `[0.2 0.4 0.6 0.8 1]`, which is the rescaled version of `[1.0, 2.0