
// Given list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {

    // We need to know the min and max values of the list
    // to determine the scale factor for the transform
    min := math.MaxFloat64
    max := math.SmallestNonzeroFloat64
    for _, v := range numbers {
        if v > max {
            max = v
        }
        if v < min {
            min = v
        }
    }

    // The scale factor is the range (max - min) divided by 1
    // so we can map the range [min, max] to [0, 1]
    scale := float64(max-min) / 1

    // Create a new list to hold the transformed values
    // and initialize all values to 0
    rescaled := make([]float64, len(numbers))

    // Loop through the original list, apply the scale factor,
    // and store the result in the rescaled list
    for i, v := range numbers {
        rescaled[i] = (v - min) / scale
    }

    return rescaled
}

