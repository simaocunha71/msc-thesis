    var start int = interval1[0]
    var end int = interval1[1]
    if interval2[0] > interval1[0]{
        start = interval2[0]
    }
    if interval2[1] < interval1[1]{
        end = interval2[1]
    }

    if start > end{
        return "NO"
    }else{
        for i := 2; i < end-start; i++{
            if end-start % i == 0{
                return "NO"
            }
        }
    }
    return "YES"
}