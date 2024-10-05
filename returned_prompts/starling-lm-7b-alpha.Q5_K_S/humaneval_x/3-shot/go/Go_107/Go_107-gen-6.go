    result := [2]int{}
    var total int = 0
    for i := 1; i <= n; i++ {
        total = total + strconv.Itoa(i) == strconv.Itoa(reverse(i)) - 1
        if i % 2 == 0 {
            result[0] += 1
        }else {
            result[1] += 1
        }
    }
    return result
}

func reverse(i int) int {
    result := 0
    for i > 0 {
        result = result * 10 + i % 10
        i = i / 10
    }
    return result
}



