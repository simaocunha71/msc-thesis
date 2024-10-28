
    start := Max(interval1[0], interval2[0])
    end := Min(interval1[1], interval2[1])
    if start > end {
        return "NO"
    }
    length := end - start + 1
    if IsPrime(length) {
        return "YES"
    } else {
        return "NO"
    }
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    sqrtN := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrtN; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func Max(x, y int) int {
    if x >