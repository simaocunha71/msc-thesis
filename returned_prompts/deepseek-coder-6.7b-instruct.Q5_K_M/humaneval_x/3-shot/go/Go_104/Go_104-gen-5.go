    result := []int{}
    for _, n := range x {
        if hasNoEvenDigit(n) {
            result = append(result, n)
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



