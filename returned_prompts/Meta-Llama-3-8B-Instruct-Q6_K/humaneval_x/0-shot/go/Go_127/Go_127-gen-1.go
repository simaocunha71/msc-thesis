```
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


The function `Intersection` takes two intervals as input. It first calculates the start and end points of the intersection. If the start point is greater than the end point, it means the intervals don't intersect, so it returns "NO".

Then it calculates the length of the intersection by subtracting the start point from the end point and adding 1.

Finally, it checks if the length is a prime number by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If it is, it returns "NO", otherwise it returns "YES".