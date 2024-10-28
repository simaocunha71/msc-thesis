```go
func Intersection(interval1 [2]int, interval2 [2]int) string {
    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end := int(math.Min(float64(interval1[1]), float64(interval2[1])))
    if start > end {
        return "NO"
    }
    length := end - start + 1
    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"
}
```


Here is the explanation of the code:

1. First, we find the start and end of the intersection of the two intervals.
2. If the start is greater than the end, it means the two intervals do not intersect, so we return "NO".
3. Then, we calculate the length of the intersection.
4. We check if the length is prime by iterating from 2 to the square root of the length, and checking if the length is divisible by any of these numbers. If it is, we return "NO".
5. If the length is not divisible by any of these numbers, it is a prime number, so we return "YES".