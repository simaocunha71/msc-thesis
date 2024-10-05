To get the smallest value and the largest value from the array, you can use the Min and Max functions from the math package in Go. Here's how you can do it:

```go
import (
    "fmt"
    "math"
)

func RescaleToUnit(numbers []float64) []float64 {
    min := math.Min(numbers...)
    max := math.Max(numbers...)
    rescaled := make([]float64, len(numbers))

    for i, n := range numbers {
        rescaled[i] = (n - min) / (max - min)
    }

    return rescaled
}
```

In this code, we define the function RescaleToUnit which takes a slice of float64 as input and returns a new slice of float64. Inside the function, we use the Min and Max functions from the math package to find the smallest and largest values in the input slice. We then iterate over the input slice using the range keyword and calculate the rescaled value for each element using the formula (n - min) / (max - min). Finally, we return the rescaled slice.

You can test the function using the following code:

```go
numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
rescaled := RescaleToUnit(numbers)
fmt.Println(rescaled) // [0, 0.25, 0.5, 0.75, 1]
```

The output will be the rescaled slice: [0.0, 0.25, 0.5, 0.75, 1.0].

Note: The Min and Max functions from the math package take variadic arguments, which means they can accept any number of arguments. In our case, we pass the entire numbers slice to these functions using the ellipsis (...) to indicate that all arguments following the first one should be passed to the function.

Also, keep in mind that the Min and Max functions return the smallest and largest values of the input arguments, respectively. So, when we call math.Min(