    var a []int
    for _, num := range x {
        if hasEvenDigit(num) {
            continue
        }
        a = append(a, num)
    }
    sort.Ints(a)
    return a
}

func hasEvenDigit(n int) bool {
    for n > 0 {
        if (n%10)%2 == 0 {
            return true
        }
        n /= 10
    }
    return false
}

