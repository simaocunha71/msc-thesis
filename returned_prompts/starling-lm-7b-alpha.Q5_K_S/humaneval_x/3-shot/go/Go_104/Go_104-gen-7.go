    result := make([]int, 0)

    for _, v := range x {
        if is_unique(v) {
            result = append(result, v)
        }
    }
    sort.Ints(result)

    return result
}

func is_unique(n int) bool {
    n_str := strconv.Itoa(n)
    for i:= 0; i< len(n_str)-1; i++ {
        if n_str[i] == n_str[i+1] && n_str[i] != '0' && n_str[i+1] != '0' {
            return false
        }
    }
    return true
}



