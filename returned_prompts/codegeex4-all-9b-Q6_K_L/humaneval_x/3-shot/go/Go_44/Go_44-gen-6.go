    result := make([]int, 0)

    for x > 0 {
        result = append([]int{x % base}, result...)
        x /= base
    }

    return strconv.Itoa(result[0])
}



