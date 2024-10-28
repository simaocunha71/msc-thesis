    result := make([]int, 0)

    for _, num := range x {
        if !hasEvenDigit(num) {
            result = append(result, num)
        }
    }

    sort.Ints(result)
    return result
}

func hasEvenDigit(n int) bool {
    str := strconv.Itoa(n)
    for _, ch := range str {
        digit, _ := strconv.Atoi(string(ch))
        if digit % 2 == 0 {
            return true
        }
    }
    return false
}



