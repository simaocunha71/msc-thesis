    var largestNegative  *int = nil
    var smallestPositive *int = nil

    for _, num := range lst{
        if num < 0 && (largestNegative == nil || num > *largestNegative){
            largestNegative = &num
        }else if num > 0 && (smallestPositive == nil || num < *smallestPositive){
            smallestPositive = &num
        }
    }

    return [2]interface{}{largestNegative, smallestPositive}
}



