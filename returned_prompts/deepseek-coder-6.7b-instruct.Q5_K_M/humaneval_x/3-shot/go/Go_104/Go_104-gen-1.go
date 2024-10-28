    var result []int
    for _, num := range x {
        if !hasEvenDigit(num) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}

func hasEvenDigit(num int) bool {
    str := strconv.Itoa(num)
    for _, char := range str {
        digit, _ := strconv.Atoi(string(char))
        if digit % 2 == 0 {
            return true
        }
    }
    return false
}



