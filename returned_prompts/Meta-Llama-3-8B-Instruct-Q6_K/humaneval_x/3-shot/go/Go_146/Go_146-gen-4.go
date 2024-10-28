    count := 0
    for _, num := range nums {
        str := strconv.Itoa(abs(num))
        if num > 10 && isOdd(str[0]) && isOdd(str[len(str)-1]) {
            count++
        }
    }
    return count
}

func isOdd(c rune) bool {
    return c-'0' % 2 == 1
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}