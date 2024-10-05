    // check if interval1 is valid
    if interval1[0] > interval1[1] {
        return "NO"
    }
    if interval2[0] > interval2[1] {
        return "NO"
    }
    // check if interval1 and interval2 intersect
    if interval1[1] < interval2[0] || interval2[1] < interval1[0] {
        return "NO"
    }
    // calculate the length of the intersection
    if interval2[0] >= interval1[0] {
        if interval2[1] <= interval1[1] {
            return "NO"
        }
        intersection_len := interval2[1] - interval1[0]
    } else {
        if interval1[1] <= interval2[1] {
            return "NO"
        }
        intersection_len := interval2[1] - interval1[0]
    }
    // check if intersection_len is a prime number
    for i := 2; i <= int(math.Sqrt(float64(intersection_len)))+1; i++ {
        if intersection_len%i == 0 {
            return "NO"
        }
    }
    return "YES"
}

































```
```

```

```

```

```
```

// You are given two intervals,
// where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
// The given intervals are closed which means that the interval (start, end)
// includes both start and end.
// Your task is to determine whether the length of Intersection of these two
// intervals is a prime number.
// Example, the Intersection of the intervals (1, 3), (2, 4) is (2, 3)
// which its length is 1, which not a prime number.
// If the length of the Intersection is a prime number, return "YES",
// otherwise, return "NO".