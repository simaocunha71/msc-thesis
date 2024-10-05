    var maxStart = int(math.Max(float64(interval1[0]), float64(interval2[0])))
    var minEnd = int(math.Min(float64(interval1[1]), float64(interval2[1])))

    if maxStart > minEnd {
        return "NO"
    }

    var len := minEnd - maxStart + 1

    if len < 2 {
        return "NO"
    }

    for i := 2; i*i <= len; i++ {
        if len%i == 0 {
            return "NO"
        }
    }
    return "YES"
}



