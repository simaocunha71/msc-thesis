```go
func Intersection(interval1 [2]int, interval2 [2]int) string {
    start, end := int(interval1[0]), int(interval1[1])
    start2, end2 := int(interval2[0]), int(interval2[1])
    
    if start > end2 || end < start2 {
        return "NO"
    }
    
    intersectionStart := int(math.Max(float64(start), float64(start2)))
    intersectionEnd := int(math.Min(float64(end), float64(end2)))
    
    if intersectionEnd < intersectionStart {
        return "NO"
    }
    
    intersectionLength := intersectionEnd - intersectionStart + 1
    
    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    
    if isPrime(intersectionLength) {
        return "YES"
    }
    return "NO"
}
```


*   We first check if the two intervals intersect by comparing their start and end points. If they do not intersect, we return "NO".
*   If they do intersect, we calculate the start and end points of the intersection.
*   We then calculate the length of the intersection by subtracting the start point from the end point and adding 1 (since the length is inclusive of both start and end points).
*   We define a helper function `isPrime` to check if a number is prime.
*   Finally, we check if the length of the intersection is prime using the `isPrime` function. If it is, we return "YES", otherwise we return "NO".