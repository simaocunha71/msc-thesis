    result := make([]int, 0)
    for _, elem := range x {
        if is_odd(strconv.Itoa(elem)) {
            result = append(result, elem)
        }
    }
    sort.Ints(result)
    return result
}

func is_odd(s string) bool {
    for _, c := range s {
        if c % 2 == 0 {
            return false
        }
    }
    return true
}



