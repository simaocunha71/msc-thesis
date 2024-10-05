    var intersection [2]int
    intersection[0] = int(math.Max(float64(interval1[0]), float64(interval2[0])))
    intersection[1] = int(math.Min(float64(interval1[1]), float64(interval2[1])))

    if intersection[0] <= intersection[1] {
        if intersection[1]-intersection[0] > 1 {
            if IsPrime(intersection[1]-intersection[0]) {
                return "YES"
            }else{
                return "NO"
            }
        }else{
            return "NO"
        }
    }else{
        return "NO"
    }
}

// Check if the given number is a prime number
// https://en.wikipedia.org/wiki/Primality_test
// https://stackoverflow.com/questions/1993392/golang-prime-number-function
func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 || n == 3 {
        return true
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false
    }

    for i := 5; i * i <= n; i += 6 {
        if n % i == 0 || n % (i + 2) == 0 {
            return false
        }
    }
    return true
}



