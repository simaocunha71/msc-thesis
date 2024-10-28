// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// 1. Convert the input list to a set for faster lookups
// 2. For each number in the list, calculate its ceiling and floor
// 3. If the ceiling or floor is in the set, return True
// 4. Otherwise, add the number to the set and continue
// 5. If no two numbers are closer to each other than the threshold, return False
func HasCloseElements(numbers []float64, threshold float64) bool {
    numberSet := make(map[float64]bool)
    for _, number := range numbers {
        lower := math.Floor(number / threshold) * threshold
        upper := math.Ceil(number / threshold) * threshold
        if numberSet[lower] || numberSet[upper] {
            return true
       