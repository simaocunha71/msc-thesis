    l = remove_duplicates(l)
    len_l := len(l)
    if len_l < 3 {
        return false
    }
    for i := 0; i < len_l; i++ {
        for j := i + 1; j < len_l; j++ {
            for k := j + 1; k < len_l; k++ {
                if l[i] + l[j] + l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}

func remove_duplicates(l []int) []int {
    result := make([]int, 0)
    for _, element := range l {
        if len(result) == 0 {
            result = append(result, element)
        } else {
            found := false
            for _, existing := range result {
                if existing == element {
                    found = true
                    break
                }
            }
            if !found {
                result = append(result, element)
            }
        }
    }
    return result
}



