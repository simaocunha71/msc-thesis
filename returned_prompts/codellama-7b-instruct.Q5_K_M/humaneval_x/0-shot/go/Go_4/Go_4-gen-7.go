import (
    "math"
)

// For a given list of input numbers, calculate Mean Absolute Deviation
// around the mean of this dataset.
// Mean Absolute Deviation is the average absolute difference between each
// element and a centerpoint (mean in this case):
// MAD = average | x - x_mean |
// >>> MeanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
// 1.0
func MeanAbsoluteDeviation(numbers []float64) float64 {
    var sum float64
    var count float64

    for _, num := range numbers {
        sum += num
        count++
    }

    mean := sum / count
    var sumDeviation float64

    for _, num := range numbers {
        sumDeviation += math.Abs(num - mean)
    }

    return sumDeviation / count
}

E:
import (
    "math"
)

// For a given list of input numbers, calculate Mean Absolute Deviation
// around the mean of this dataset.
// Mean Absolute Deviation is the average absolute difference between each
// element and a centerpoint (mean in this case):
// MAD = average | x - x_mean |
// >>> MeanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
// 1.0
func MeanAbsoluteDeviation(numbers []float64) float64 {
    var sum float64
    var count float64

    for _, num := range numbers {
        sum += num
        count++
    }

    mean := sum / count
    var sumDeviation float64

    for _, num := range numbers {
        sumDeviation += math.Abs(num - mean)
    }

    return sumDeviation / count
}

F:
import (
    "math"
)

// For a given list of input numbers, calculate Mean Absolute Deviation
// around the mean of this dataset.
// Mean Absolute Deviation is the average absolute difference between each
// element and a centerpoint (mean in this case):
//