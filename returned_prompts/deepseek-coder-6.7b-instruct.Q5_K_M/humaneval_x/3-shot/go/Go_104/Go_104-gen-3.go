    result := make([]int, 0)
    for _, num := range x {
        if hasNoEvenDigit(num) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}

func hasNoEvenDigit(n int) bool {
    for n > 0 {
        if (n%10)%2 == 0 {
            return false
        }
        n = n / 10
    }
    return true
}



