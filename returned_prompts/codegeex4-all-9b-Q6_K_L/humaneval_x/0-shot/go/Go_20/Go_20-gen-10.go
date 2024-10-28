func FindClosestElements(numbers []float64) [2]float64 {
    var closestPair [2]float64
    var minDiff float64 = math.MaxFloat64

    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < minDiff {
                minDiff = diff
                closestPair[0] = numbers[i]
                closestPair[1] = numbers[j]
            }
        }
    }

    return closestPair
}