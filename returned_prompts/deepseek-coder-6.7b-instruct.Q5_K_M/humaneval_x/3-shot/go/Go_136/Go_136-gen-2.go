    var largestNegative *int = nil
    var smallestPositive *int = nil

    for _, number := range lst {
        if number < 0 && (largestNegative == nil || number > *largestNegative) {
            largestNegative = &number
        } else if number > 0 && (smallestPositive == nil || number < *smallestPositive) {
            smallestPositive = &number
        }
    }

    return [2]interface{}{largestNegative, smallestPositive}
}



