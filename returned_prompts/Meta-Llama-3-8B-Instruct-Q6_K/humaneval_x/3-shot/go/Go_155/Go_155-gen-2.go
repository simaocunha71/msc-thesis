    var even int = 0
    var odd int = 0
    str := strconv.Itoa(num)
    for _, c := range str {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}