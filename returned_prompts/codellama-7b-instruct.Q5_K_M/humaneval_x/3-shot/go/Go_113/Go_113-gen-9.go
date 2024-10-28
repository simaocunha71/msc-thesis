    result := make([]string, 0)
    for _, element := range lst {
        count := 0
        for _, c := range element {
            if int(c - '0') % 2 != 0 {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %d in the string %d of the input.", count, len(element)))
    }
    return result
}



