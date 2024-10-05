    result := make([]int, 0)

    for _, num := range x {
        if hasNoEvenDigit(num) {
            result = append(result, num)
        }
    }

    sort.Ints(result)
    return result
}

func hasNoEvenDigit(num int) bool {
    digits := strconv.Itoa(num)

    for _, digit := range digits {
        intDigit, _ := strconv.Atoi(string(digit))
        if intDigit % 2 == 0 {
            return false
        }
    }

    return true
}



