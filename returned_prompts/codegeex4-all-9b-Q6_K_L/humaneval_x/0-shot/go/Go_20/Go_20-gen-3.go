func FindClosestElements(numbers []float64) [2]float64 {
    if len(numbers) < 2 {
        return [2]float64{}
    }

    // Sort the numbers in ascending order
    sort.Float64s(numbers)

    // Initialize the closest pair and the smallest difference
    closestPair := [2]float64{numbers[0], numbers[1]}
    smallestDiff := numbers[1] - numbers[0]

    // Iterate through the sorted numbers to find the closest pair
    for i := 2; i < len(numbers); i++ {
        diff := numbers[i] - numbers[i-1]
        if diff < smallestDiff {
            smallestDiff = diff
            closestPair = [2]float64{numbers[i-1], numbers[i]}
        }
    }

    return closestPair
}