    var result = make([]int, 0)

    for _, v := range x {
        if isUniqueDigits(v) {
            result = append(result, v)
        }
    }

    sort.Ints(result)

    return result
}

func isUniqueDigits(v int) bool {
    strV := strconv.Itoa(v)
    for i := 0; i < len(strV); i++ {
        if strV[i] - '0' % 2 == 0 {
            return false
        }
    }
    return true
}



