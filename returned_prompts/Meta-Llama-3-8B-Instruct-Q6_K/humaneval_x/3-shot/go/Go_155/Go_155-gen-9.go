    var even int = 0
    var odd int = 0
    numStr := strconv.Itoa(abs(num))
    for _, c := range numStr {
        digit, err := strconv.Atoi(string(c))
        if err != nil {
            panic(err)
        }
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}