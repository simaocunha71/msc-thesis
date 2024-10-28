    var intersection_start, intersection_end int

    if interval1[0] > interval2[0] {
        intersection_start = interval1[0]
    } else {
        intersection_start = interval2[0]
    }

    if interval1[1] < interval2[1] {
        intersection_end = interval1[1]
    } else {
        intersection_end = interval2[1]
    }

    if intersection_start > intersection_end {
        return "NO"
    }

    if isPrime(intersection_end-intersection_start+1){
        return "YES"
    }

    return "NO"
}

func isPrime(n int) bool{
    if n <= 1{
        return false
    }

    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n % i == 0{
            return false
        }
    }
    return true
}