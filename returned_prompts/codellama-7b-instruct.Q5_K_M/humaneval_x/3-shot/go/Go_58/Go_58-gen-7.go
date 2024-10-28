    result := make([]int, 0)

    for _, x := range l1 {
        if !contains(l2, x) {
            continue
        }
        result = append(result, x)
    }

    sort.Ints(result)
    return result
}

func contains(s []int, e int) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}



