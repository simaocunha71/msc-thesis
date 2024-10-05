    result := make([]int, 0)
    appeared := make(map[int]bool)

    for _, number := range numbers {
        if appeared[number] {
            continue
        }
        appeared[number] = true
        result = append(result, number)
    }
    return result
}



