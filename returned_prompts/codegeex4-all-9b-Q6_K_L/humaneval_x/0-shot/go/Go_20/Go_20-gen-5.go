func FindClosestElements(numbers []float64) [2]float64 {
    sort.Float64s(numbers)
    minDiff := math.MaxFloat64
    result := [2]float64{}
    for i := 0; i < len(numbers)-1; i++ {
        diff := numbers[i+1] - numbers[i]
        if diff < minDiff {
            minDiff = diff
            result = [2]float64{numbers[i], numbers[i+1]}
        }
    }
    return result
}
