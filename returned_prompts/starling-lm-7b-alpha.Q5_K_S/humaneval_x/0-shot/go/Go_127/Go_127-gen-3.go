    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    return strconv.FormatBool(isPrime(interval1[1]-interval2[0]))
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}


*/






func Intersection(interval1 [2]int, interval2 [2]int) string {
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    return strconv.FormatBool(isPrime(interval1[1]-interval2[0]))
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

























































































































































































































