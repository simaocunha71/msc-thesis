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
    if math.IsNaN(number) || math.IsInf(number,1)||math.IsInf(number,-1){
        return number
    }else{
        if number < math.MaxFloat64-1 && number >= 0 {
            return float64(int64_t(number)) - 1
        }else if number > math.MaxFloat64+1 && number <= math.MaxFloat64/2 {
            return (float64(int64_t(math.MaxFloat64))) + int64_t(number)
        }else{
            return float64(int64_t(number)) - 1
        }
    }
}