```go
import (
    "math"
)

func Factorize(n int) []int {
    factors := make([]int, 0)
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        count := 0
        for n%i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            factors = append(factors, int32(i))
            for count > 0 {
