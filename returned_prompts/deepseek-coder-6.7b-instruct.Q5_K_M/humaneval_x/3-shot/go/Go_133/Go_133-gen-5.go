    sum := 0

    for _, num := range lst {
        ceil := int(math.Ceil(num))
        sum += ceil * ceil
    }

    return sum
}



