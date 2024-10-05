    a,b := max(interval1[0],interval2[0]), min(interval1[1],interval2[1])
    if a>b {
        return "NO"
    }
    if a==b {
        return "YES"
    }
    if isPrime(b-a) {
        return "YES"
    }else{
        return "NO"
    }
}




func max(a,b int) int {
    if a>b {
        return a
    }else{
        return b
    }
}

func min(a,b int) int {
    if a<b {
        return a
    }else{
        return b
    }
}

func isPrime(n int) bool {
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}





