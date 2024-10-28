    result := make([]string, len(lst))
    for i := 0; i < len(lst); i++ {
        var count int = 0
        for _, c := range lst[i] {
            if string(c) == "1" {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %d in the string %d of the %d input.", count, i + 1, len(lst))
    }
    return result
}



