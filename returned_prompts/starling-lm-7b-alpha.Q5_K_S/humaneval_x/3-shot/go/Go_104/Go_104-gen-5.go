    result := make([]int, 0)

    for _, i := range x {
        if is_odd_digits(i) {
            result = append(result, i)
        }
    }

    sort.Ints(result)
    return result
}

func is_odd_digits(i int) bool {
    s := strconv.Itoa(i)
    for _, c := range s {
        if int(c)-48%2 == 0 {
            return false
        }
    }
    return true
}



