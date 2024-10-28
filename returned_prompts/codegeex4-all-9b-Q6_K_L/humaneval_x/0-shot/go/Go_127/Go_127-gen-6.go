func Intersection(interval1 [2]int, interval2 [2]int) string {
    length := 0
    if interval1[0] > interval2[0] {
        if interval1[0] <= interval2[1] {
            length = interval2[1] - interval1[0] + 1
        }
    } else {
        if interval2[0] <= interval1[1] {
            length = interval1[1] - interval2[0] + 1
        }
    }
    if length == 0 {
        return "NO"
    }
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3})) // "NO"
    fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4})) // "NO"
    fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5})) // "YES"
}