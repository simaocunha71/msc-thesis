    var positiveNumbers []int

    for _, number := range l {
        if number > 0 {
            positiveNumbers = append(positiveNumbers, number)
        }
    }

    return positiveNumbers
}



