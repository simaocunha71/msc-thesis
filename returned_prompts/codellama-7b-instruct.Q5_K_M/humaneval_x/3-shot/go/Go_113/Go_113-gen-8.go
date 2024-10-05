    result := make([]string, len(lst))
    for i, s := range lst {
        odd := 0
        for _, c := range s {
            if c-'0'%2 == 1 {
                odd += 1
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %d in the string %d of the %s.", odd, i, "input.")
    }
    return result
}



