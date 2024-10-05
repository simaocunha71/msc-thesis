    var largestNegative  *int = nil
    var smallestPositive *int = nil

    for _, v := range lst {
        if v > 0 {
            if smallestPositive == nil || v < *smallestPositive {
                smallestPositive = &v
            }
        } else if v < 0 {
            if largestNegative == nil || v > *largestNegative {
                largestNegative = &v
            }
        }
    }

    return [2]interface{}{largestNegative, smallestPositive}
}



