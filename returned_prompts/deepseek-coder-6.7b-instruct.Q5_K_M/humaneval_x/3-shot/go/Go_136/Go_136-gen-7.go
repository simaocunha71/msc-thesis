    var largestNegativeInt *int = nil
    var smallestPositiveInt *int = nil

    for _, number := range lst {
        if number < 0 && (largestNegativeInt == nil || number > *largestNegativeInt) {
            largestNegativeInt = &number
        } else if number > 0 && (smallestPositiveInt == nil || number < *smallestPositiveInt) {
            smallestPositiveInt = &number
        }
    }
    return [2]interface{}{largestNegativeInt, smallestPositiveInt}
}



