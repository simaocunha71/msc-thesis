    if interval1[0] > interval2[1] || interval2[0] > interval1[1]{
        return "NO"
    }
    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end := int(math.Min(float64(interval1[1]), float64(interval2[1])))
    if end < start{
        return "NO"
    }
    for i := start; i <= end; i++{
        if isPrime(i){
            return "YES"
        }
    }
    return "NO"
}
func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



