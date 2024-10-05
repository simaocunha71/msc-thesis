func FindClosestElements(numbers []float64) [2]float64 {
    if len(numbers) < 2 {
        panic("The list must contain at least two numbers")
    }
    closest := [2]float64{numbers[0], numbers[1]}
    minDiff := math.Abs(numbers[0] - numbers[1])
    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < minDiff {
                minDiff = diff
                closest[0] = numbers[i]
                closest[1] = numbers[j]
            }
        }
    }
    return closest
}