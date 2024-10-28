    sum := 0
    for _, num := range lst {
        ceilNum := int(math.Ceil(num))
        sum += ceilNum * ceilNum
    }
    return sum
}



