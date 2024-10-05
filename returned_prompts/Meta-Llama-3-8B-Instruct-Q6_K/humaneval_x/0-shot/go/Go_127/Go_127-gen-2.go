Here is the solution:
```go
func Intersection(interval1 [2]int, interval2 [2]int) string {
    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end := int(math.Min(float64(interval1[1]), float64(interval2[1])))
    
    if start > end {
        return "NO"
    }
    
    length := end - start + 1
    
    isPrime := true
    for i := 2; i * i <= length; i++ {
        if length%i == 0 {
            isPrime = false
            break
        }
    }
    
    if isPrime {
        return "YES"
    } else {
        return "NO"
    }
}
```
Explanation:

1. First, we calculate the start and end points of the intersection by taking the maximum of the two start points and the minimum of the two end points.
2. If the start point is greater than the end point, it means the intervals don't intersect, so we return "NO".
3. We calculate the length of the intersection by subtracting the start point from the end point and adding 1 (because the end point is inclusive).
4. We check if the length is a prime number by iterating from 2 to the square root of the length and checking if the length is divisible by any of the numbers. If it is, we set `isPrime` to `false` and break the loop.
5. If `isPrime` is still `true` after the loop, we return "YES", otherwise we return "NO".