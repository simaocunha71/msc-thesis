    var start int = Max(interval1[0], interval2[0])
    var end int = Min(interval1[1], interval2[1])
    var length int = end - start + 1
    
    if length < 2 {
        return "NO"
    }
    
    for i := 2; i*i <= length; i++ {
        if length % i == 0 {
            return "NO"
        }
    }
    return "YES"
}

func Max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func Min(x, y int) int {
    if x < y {
        return x
    }
    return y
}


