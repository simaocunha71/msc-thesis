
    // We need to find the intersection of the two intervals.
    // And then we need to check if the length of the intersection
    // is a prime number.

    // Firstly, find the intersection.
    var start, end int
    if interval1[0] > interval2[0] {
        start = interval1[0]
    } else {
        start = interval2[0]
    }

    if interval1[1] < interval2[1] {
        end = interval1[1]
    } else {
        end = interval2[1]
    }

    // If the start is greater than the end,
    // it means that the two intervals don't intersect.
    if start > end {
        return "NO"
    }

    // Now we know that the two intervals intersect.
    // The length of the intersection is end - start.
    length := end - start + 1

    // Check if the length is a prime number.
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

// 