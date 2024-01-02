import (
    "math"
)

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
// >>> TruncateNumber(3.5)
// 0.5
func TruncateNumber(number float64) float64 {
    if number == math.MaxFloat64 || number < 0.0 || number >= math.MinFloat64 {
        // If the input is zero or inf, return it (the decimals are always zero in that case).
        return number
    }
    
    var iPart = 1.0 / math.Pow(2.0, float64(math.Log(number) / math.Ln2))
    
    if !floatToInt(iPart * number, &iPart, number) {
        // If the input is not a integer (floating point error) return 1/0
        return 1.0 / 0.0
    }
    
    return iPart
}