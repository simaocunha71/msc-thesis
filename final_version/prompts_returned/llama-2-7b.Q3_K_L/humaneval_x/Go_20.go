
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {
    if len(numbers) < 2 {
        return nil
    }

    minDelta := math.MaxFloat64
    minFound := numbers[0]
    
    for i, n := range numbers {
        delta := math.Abs(n - minFound)
        
        if delta < minDelta && delta != 0 {
            minFound = n
            minDelta = delta
        } else {
            return []float64{}
        }
    }
    
    return [2]float64{minFound, minFound}
}