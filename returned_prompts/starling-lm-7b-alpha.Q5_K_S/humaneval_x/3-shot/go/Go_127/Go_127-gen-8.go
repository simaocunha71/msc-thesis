    start, end := math.Min(float64(interval1[0]), float64(interval1[1])), math.Max(float64(interval1[0]), float64(interval1[1]))
    start1, end1 := math.Min(float64(interval2[0]), float64(interval2[1])), math.Max(float64(interval2[0]), float64(interval2[1]))
    start2, end2 := math.Max(start, start1), math.Min(end, end1)
    if start2 > end2 {
        return "NO"
    }
    length := end2 - start2 + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}


func isPrime(num float64) bool {
    if num == 2 {
        return true
    }
    if num < 2 || num%2 == 0 {
        return false
    }
    for i := 3; i * i <= num; i += 2 {
        if num%i == 0 {
            return false
        }
    }
    return true
}



































































































































































































































