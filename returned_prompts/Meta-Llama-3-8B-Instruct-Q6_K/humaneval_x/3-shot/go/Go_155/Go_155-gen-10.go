    var even int = 0
    var odd int = 0
    s := strconv.Itoa(num)
    for _, c := range s {
        d, _ := strconv.Atoi(string(c))
        if d % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}