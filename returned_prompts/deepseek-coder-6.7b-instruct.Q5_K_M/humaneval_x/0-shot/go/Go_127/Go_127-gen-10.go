
    // Given two intervals.
    start1, end1 := interval1[0], interval1[1]
    start2, end2 := interval2[0], interval2[1]

    // Determine the intersection of the two intervals.
    start := max(start1, start2)
    end := min(end1, end2)

    // If the two intervals don't intersect, return "NO".
    if start > end {
        return "NO"
    }

    // Determine the length of the intersection.
    length := end - start + 1

    // Determine whether the length of the intersection is a prime number.
    if length < 2 {
        return "NO"
    }
    for i := 2; i * i <= length; i++ {
        if length % i == 0 {
            return "NO"
        }
    }

    // If the length is a prime number, return "YES".
    return "YES"
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

```



## Python 

```python

def Intersection(interval1, interval2):

    start1, end1 = interval1
    start2, end2 = interval2

    start = max(start1, start2)
    end = min(end1, end2)

    if start > end:
        return "NO"

    length = end - start + 1

    if length < 2:
        return "NO"

    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"

```



## Javascript 

```javascript

function Intersection(interval1, interval2) {

    var start1 = interval1[0], end1 = interval1[1];
    var start2 = interval2