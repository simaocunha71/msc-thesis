    var largestNegative, smallestPositive interface{}
    largestNegativeVal, smallestPositiveVal := -math.MaxInt32, math.MaxInt32
    for _, num := range lst {
        if num < 0 && num > int(largestNegativeVal) {
            largestNegative = num
            largestNegativeVal = num
        } else if num > 0 && num < smallestPositiveVal {
            smallestPositive = num
            smallestPositiveVal = num
        }
    }
    if largestNegativeVal == -math.MaxInt32 {
        largestNegative = nil
    }
    if smallestPositiveVal == math.MaxInt32 {
        smallestPositive = nil
    }
    return [2]interface{}{largestNegative, smallestPositive}
}