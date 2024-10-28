    result := make([]int, 0)

    for _, v := range x {
        if hasEvenDigit(v) == false {
            result = append(result, v)
        }
    }

    sort.Ints(result)
    return result
}

func hasEvenDigit(n int) bool {
    s := strconv.Itoa(n)
    for _, v := range s {
        if int(v) % 2 == 0 {
            return true
        }
    }
    return false
}




