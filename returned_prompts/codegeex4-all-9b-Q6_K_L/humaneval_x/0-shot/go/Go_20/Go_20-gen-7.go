func FindClosestElements(numbers []float64) [2]float64 {
    var closestElements [2]float64
    minDifference := math.MaxFloat64

    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            difference := math.Abs(numbers[i] - numbers[j])
            if difference < minDifference {
                minDifference = difference
                closestElements[0] = numbers[i]
                closestElements[1] = numbers[j]
            }
        }
    }

    return closestElements
}