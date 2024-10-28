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

Review:

The function name `HasCloseElements` is not descriptive enough. It should convey what the function does. A better name could be `HasTwoNumbersCloserThanThreshold`.

The function uses two nested loops to compare all pairs of numbers in the input slice. This can be optimized by sorting the slice first, then only comparing adjacent elements in the sorted slice.

The function returns `true` as soon as it finds two numbers closer than the threshold. It would be more efficient to break out of the loops as soon as it finds a pair of numbers closer than the threshold.

import (
    "math"
)

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
//