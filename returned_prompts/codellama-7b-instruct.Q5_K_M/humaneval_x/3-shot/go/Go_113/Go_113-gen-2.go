    result := make([]string, 0)
    for _, s := range lst {
        var count int = 0
        for _, r := range s {
            if int(r)%2 == 1 {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %d in the string %d of the input.", count, len(s)))
    }
    return result
}



