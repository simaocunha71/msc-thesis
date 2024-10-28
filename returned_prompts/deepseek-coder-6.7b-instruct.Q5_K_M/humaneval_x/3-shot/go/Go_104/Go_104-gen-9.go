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
    digits := strconv.Itoa(n)
    for _, digit := range digits {
        num, _ := strconv.Atoi(string(digit))
        if num % 2 == 0 {
            return true
        }
    }
    return false
}



