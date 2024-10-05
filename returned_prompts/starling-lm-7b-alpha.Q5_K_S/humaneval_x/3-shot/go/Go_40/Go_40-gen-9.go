    distinct_elements := make(map[int]int)
    for _, v := range l {
        if _, ok := distinct_elements[v]; !ok {
            distinct_elements[v] = 1
        }else {
            distinct_elements[v] += 1
        }
    }
    for i := 0; i < len(l); i++ {
        for j := i + 1; j < len(l); j++ {
            for k := j + 1; k < len(l); k++ {
                if l[i] + l[j] + l[k] == 0 {
                    if distinct_elements[l[i]] > 1 && distinct_elements[l[j]] > 1 && distinct_elements[l[k]] > 1 {
                        return true
                    }
                }
            }
        }
    }
    return false
}



