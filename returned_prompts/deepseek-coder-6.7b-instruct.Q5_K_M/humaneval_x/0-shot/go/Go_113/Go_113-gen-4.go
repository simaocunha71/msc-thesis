    result := make([]string, len(lst))
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if int(c-'0')%2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %don the string %d of the input.", count, count)
    }
    return result
}

