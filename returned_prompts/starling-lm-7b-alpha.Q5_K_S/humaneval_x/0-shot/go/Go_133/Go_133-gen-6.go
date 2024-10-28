    // round each number in the list to the upper int
    for i := 0; i < len(lst); i++ {
        lst[i] = math.Ceil(lst[i])
    }
    // calculate the sum of squared numbers in the list
    sum := 0
    for i := 0; i < len(lst); i++ {
        sum += int(lst[i]*lst[i])
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        sum += int(math.Ceil(v) * math.Ceil(v))
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        sum += (math.Ceil(v) * math.Ceil(v))
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        v1 := math.Ceil(v)
        sum += int(v1 * v1)
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        v1 := int(math.Ceil(v))
        sum += v1 * v1
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        v1 := int(math.Ceil(v))
        sum += v1 * v1
    }
    return sum
}




func SumSquares(lst []float64) int {
    sum := 0
    for _, v := range lst {
        v1 := math.Ceil(v)
        sum += int(v1 * v1)
    }
   