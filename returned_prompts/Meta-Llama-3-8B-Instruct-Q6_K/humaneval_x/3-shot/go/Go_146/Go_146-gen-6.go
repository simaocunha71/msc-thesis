    var count int
    for _, num := range nums {
        str := strconv.Itoa(abs(num))
        if num > 10 && (str[0] % 2 != 0 && str[len(str)-1] % 2 != 0) {
            count++
        }
    }
    return count
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}