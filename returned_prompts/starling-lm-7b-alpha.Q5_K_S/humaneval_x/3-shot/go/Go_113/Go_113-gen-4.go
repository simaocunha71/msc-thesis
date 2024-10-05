    result := make([]string, 0)

    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", count, v, count, len(lst)))
    }
    return result
}



