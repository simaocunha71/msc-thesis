    sum := 0
    for _, num := range lst {
        rounded := int(math.Ceil(num))
        sum += rounded * rounded
    }
    return sum
}



