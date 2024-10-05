    type Point struct {
        Value int
        Index int
    }
    type ByValue []Point
    sort.Sort(ByValue(
        append(
            []Point(nil),
            make([]Point, len(nums)),
        )
    ))
    return append(
        []int(nil),
        make([]int, len(nums))...
    )
}



