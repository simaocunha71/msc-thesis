import (
    "math"
)

func TruncateNumber(number float64) float64 {
    return math.Abs(number - float64(int(number)))
}


A: import (
    "math"
)

// TruncateNumber returns the fractional part of the given number.
func TruncateNumber(number float64) float64 {
    return number - float64(int(number))
}

