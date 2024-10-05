    var even int = 0
    var odd int = 0
    num_str := strconv.Itoa(num)
    for _, c := range num_str {
        if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}