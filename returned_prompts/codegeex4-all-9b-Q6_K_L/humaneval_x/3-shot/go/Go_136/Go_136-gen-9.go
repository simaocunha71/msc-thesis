    var largest_negative int = lst[0]
    var smallest_positive int = lst[0]

    for _, i := range lst {
        if i > 0 && i < smallest_positive {
            smallest_positive = i
        } else if i < 0 && i > largest_negative {
            largest_negative = i
        }
    }

    if smallest_positive == lst[0] {
        smallest_positive = 0
    }

    if largest_negative == lst[0] {
        largest_negative = 0
    }

    return [2]interface{}{largest_negative, smallest_positive}
}



