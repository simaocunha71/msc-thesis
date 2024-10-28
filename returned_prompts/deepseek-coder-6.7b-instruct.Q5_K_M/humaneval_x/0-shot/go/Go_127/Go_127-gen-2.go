
    // Your code here
    // determine whether the length of Intersection of these two
    // intervals is a prime number.
    // If the length of the Intersection is a prime number, return 
    // "YES", otherwise, return 
    // "NO".
    // If the two intervals don't intersect, return 
    // "NO".

    // find the intersection of two intervals
    var intersection [2]int
    if interval1[0] > interval2[0] {
        intersection[0] = interval1[0]
    } else {
        intersection[0] = interval2[0]
    }
    if interval1[1] < interval2[1] {
        intersection[1] = interval1[1]
    } else {
        intersection[1] = interval2[1]
    }

    // if the intervals do not intersect
    if intersection[0] > intersection[1] {
        return "NO"
    }

    // calculate the length of the intersection
    length := intersection[1] - intersection[0]

    // check if the length is a prime number
    if length < 2 {
        return "NO"
    }
    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"
}

```

## Code

```go
package kata

import "math"

func IsPrime(n int) bool {
    if n == 2 {
        return true
    }
    if n % 2 == 0 || n == 1 {
        return false
    }
    sqrt := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrt; i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func Intersection(interval1 [2]int, interval2 [2]int) string {
    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end :