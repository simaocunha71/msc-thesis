    start, end := min(interval1[0], interval1[1]), max(interval1[0], interval1[1])
    start2, end2 := min(interval2[0], interval2[1]), max(interval2[0], interval2[1])

    if end < start2 || end2 < start {
        return "NO"
    }

    start3, end3 := max(start, start2), min(end, end2)
    if end3 > start3 {
        return "YES"
    }
    return "NO"
}



