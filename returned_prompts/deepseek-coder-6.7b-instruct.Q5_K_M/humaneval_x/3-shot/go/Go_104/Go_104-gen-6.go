    var res  []int

    for _, num := range x {
        if !hasEvenDigit(num) {
            res = append(res, num)
        }
    }

    sort.Ints(res)
    return res
}

func hasEvenDigit(num int) bool {
    digits := strconv.Itoa(num)
    for _, digit := range digits {
        n, _ := strconv.Atoi(string(digit))
        if n % 2 == 0 {
            return true
        }
    }
    return false
}


