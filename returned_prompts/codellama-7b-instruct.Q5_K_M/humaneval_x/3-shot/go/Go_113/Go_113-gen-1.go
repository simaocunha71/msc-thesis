    result := make([]string, 0)
    for _, s := range lst {
        count := 0
        for _, c := range s {
            if string(c) == "1"{
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %d in the str%dng %d of the %dinput.",count, len(s), len(s), len(lst)))
    }
    return result
}



