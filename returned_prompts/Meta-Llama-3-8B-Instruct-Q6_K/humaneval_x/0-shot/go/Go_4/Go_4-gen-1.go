Here is a Go function that calculates the Mean Absolute Deviation (MAD) of a given list of numbers:

```go
import (
    "math"
)

func MeanAbsoluteDeviation(numbers []float64) float64 {
    mean := getMean(numbers)
    var sum float64
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}

func getMean(numbers []float64) float64 {
    sum := 0.0
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}
```

In the `MeanAbsoluteDeviation` function, we first calculate the mean of the input numbers using the `getMean` function. Then, we iterate over the input numbers, calculate the absolute difference between each number and the mean, and add it to a running sum. Finally, we return the sum divided by the length of the input numbers.

The `getMean` function simply calculates the mean of the input numbers by summing them up and dividing by the length of the input numbers. 

You can use this function like this:

```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
result := MeanAbsoluteDeviation(numbers)
fmt.Println(result)
```


This will calculate and print the Mean Absolute Deviation of the input numbers. 

Note that this function assumes that the input list is not empty. If the input list is empty, it will panic when trying to calculate the mean. If you want to handle the case where the input list is empty, you can add a check at the beginning of the `MeanAbsoluteDeviation` function:

```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    if len(numbers) == 0 {
        return 0.0
    }
    mean := getMean(numbers)
    // ...
}
```


This will return 0.0 if the input list is empty. You can adjust this behavior to suit your needs. 

Also note that this function uses the `math.Abs` function to calculate the absolute difference between each number and the mean. This function returns a `float64` value, so the result of the `MeanAbsoluteDeviation` function will also be a `float64` value. 

I hope this helps! Let me know if you have any questions. 

Please note that the above code