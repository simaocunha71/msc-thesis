func FindClosestElements(numbers []float64) [2]float64 {
    // Sort the numbers in ascending order
    sort.Float64s(numbers)

    // Initialize variables to store the smallest difference and the two closest numbers
    smallestDifference := math.MaxFloat64
    closestNumbers := [2]float64{}

    // Iterate through the numbers to find the two closest ones
    for i := 0; i < len(numbers)-1; i++ {
        difference := numbers[i+1] - numbers[i]
        if difference < smallestDifference {
            smallestDifference = difference
            closestNumbers[0] = numbers[i]
            closestNumbers[1] = numbers[i+1]
        }
    }

    return closestNumbers
}