func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        sum += int(math.Ceil(v)) * int(math.Ceil(v))
    }
    return sum
}