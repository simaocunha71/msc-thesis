    var start int
    var end int

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

    if start > end {
        return "NO"
    }

    length := end - start + 1
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



