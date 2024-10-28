    result := []int{}
    for _, number := range x {
        if !hasEvenDigit(number) {
            result = append(result, number)
        }
    }
    sort.Ints(result)
    return result
}

func hasEvenDigit(number int) bool {
    digits := strconv.Itoa(number)
    for _, digit := range digits {
        num, _ := strconv.Atoi(string(digit))
        if num % 2 == 0 {
            return true
        }
    }
    return false
}



