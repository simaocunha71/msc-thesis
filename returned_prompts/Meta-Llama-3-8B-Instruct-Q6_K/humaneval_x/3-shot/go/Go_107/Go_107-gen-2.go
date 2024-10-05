    var even int = 0
    var odd int = 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == strconv.Itoa(i)[::-1] {
            if i % 2 == 0 {
                even++
            }else{
                odd++
            }
        }
    }
    return [2]int{even, odd}
}