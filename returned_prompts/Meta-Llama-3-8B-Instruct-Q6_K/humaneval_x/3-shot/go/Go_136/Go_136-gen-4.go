    var result [2]interface{}
    negativeMax := -math.MaxInt32
    positiveMin := math.MaxInt32

    for _, num := range lst {
        if num < 0 {
            if num > negativeMax {
                negativeMax = num
            }
        } else if num > 0 {
            if num < positiveMin {
                positiveMin = num
            }
        }
    }

    if negativeMax == -math.MaxInt32 {
        result[0] = nil
    } else {
        result[0] = negativeMax
    }

    if positiveMin == math.MaxInt32 {
        result[1] = nil
    } else {
        result[1] = positiveMin
    }

    return result
}