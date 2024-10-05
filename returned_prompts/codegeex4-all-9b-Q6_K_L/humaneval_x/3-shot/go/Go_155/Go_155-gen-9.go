    var even, odd int
    abs_num := strconv.Itoa(abs(num))
    for _, i := range abs_num {
        if i%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}



