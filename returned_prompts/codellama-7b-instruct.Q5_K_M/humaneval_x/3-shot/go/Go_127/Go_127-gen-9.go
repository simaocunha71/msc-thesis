    if interval1[0] > interval1[1] || interval2[0] > interval2[1]{
        return "NO"
    }

    if (interval1[0] <= interval2[1] && interval1[1] >= interval2[0]){
        if interval1[0] >= interval2[0] && interval1[1] <= interval2[1]{
            return "YES"
        }
        start := max(interval1[0], interval2[0])
        end := min(interval1[1], interval2[1])
        if end - start == 0{
            return "NO"
        }
        return "YES"

    }

    return "NO"
}



