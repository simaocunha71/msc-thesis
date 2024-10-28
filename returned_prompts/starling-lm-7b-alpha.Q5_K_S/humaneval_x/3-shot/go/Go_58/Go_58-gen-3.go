    result := make([]int, 0)
    result = append(result, l1...)
    result = append(result, l2...)
    sort.Ints(result)

    i := 0
    for i < len(result) - 1 {
        if result[i] == result[i+1] {
            result = append(result[:i], result[i+1:]...)
            i--
        }
        i += 1
    }

    return result[:len(result)-1]
}



