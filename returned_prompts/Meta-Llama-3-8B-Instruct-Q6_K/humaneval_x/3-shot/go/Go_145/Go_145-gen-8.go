    type Point struct {
        val int
        idx int
    }

    points := make([]Point, len(nums))
    for i, v := range nums {
        points[i] = Point{v, i}
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].val+points[i].idx != points[j].val+points[j].idx {
            return points[i].val+points[i].idx < points[j].val+points[j].idx
        }
        return points[i].idx < points[j].idx
    })

    result := make([]int, len(nums))
    for i, p := range points {
        result[i] = p.val
    }
    return result
}



