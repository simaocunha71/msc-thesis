    result := make([]int, 0)
    for _, v := range x {
        if is_valid(v) {
            result = append(result, v)
        }
    }
    sort.Ints(result)

    return result
}

func is_valid(n int) bool {
    s := strconv.Itoa(n)
    for _, c := range s {
        if int(c) % 2 == 0 {
            return false
        }
    }
    return true
}



