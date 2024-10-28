func FindClosestElements(numbers []float64) [2]float64 {
    minDiff := math.MaxFloat64
    result := [2]float64{}
    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < minDiff {
                minDiff = diff
                result = [2]float64{numbers[i], numbers[j]}
            }
        }
    }
    return result
}