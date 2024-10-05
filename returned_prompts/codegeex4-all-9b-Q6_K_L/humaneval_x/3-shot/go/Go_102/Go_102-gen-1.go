    var total float64 = 0
    for _, number := range numbers{
        total += float64(number)
    }
    return total / float64(len(numbers))
}

// Given a list of numbers, it should return the average of all the odd numbers in the list.
// >>>