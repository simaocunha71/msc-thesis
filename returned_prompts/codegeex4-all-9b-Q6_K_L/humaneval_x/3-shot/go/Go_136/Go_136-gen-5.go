    var smallestPositive int
    var largestNegative int
    var smallestPositiveFound bool
    var largestNegativeFound bool

    for _, num := range lst {
        if num > 0 {
            if !smallestPositiveFound || num < smallestPositive {
                smallestPositive = num
                smallestPositiveFound = true
            }
        } else if num < 0 {
            if !largestNegativeFound || num > largestNegative {
                largestNegative = num
                largestNegativeFound = true
            }
        }
    }

    return [2]interface{}{largestNegativeFound && largestNegative, smallestPositiveFound && smallestPositive}
}

