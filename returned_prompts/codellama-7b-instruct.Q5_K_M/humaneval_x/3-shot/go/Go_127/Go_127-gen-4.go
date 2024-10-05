    var start_point int
    var end_point int
    var result string

    if interval1[0] <= interval1[1] && interval2[0] <= interval2[1] {
        start_point = max(interval1[0], interval2[0])
        end_point = min(interval1[1], interval2[1])

        if start_point <= end_point {
            result = "YES"
        }
    }else{
        result = "NO"
    }
    return result
}



