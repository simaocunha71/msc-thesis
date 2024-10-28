    result := make([]string, len(lst))

    for i := 0; i < len(lst); i++ {
        var count int = 0
        for _, c := range lst[i] {
            if c%2 != 0 {
                count += 1
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %v in the string %v of the input.", count, i)
    }
    return result
}



