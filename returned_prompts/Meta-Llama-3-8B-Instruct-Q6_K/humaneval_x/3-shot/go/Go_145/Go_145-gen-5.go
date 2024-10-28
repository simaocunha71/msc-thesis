    type Point struct {
        val  int
        orig int
    }
    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i].val = num
        points[i].orig = i
    }
    sort.Slice(points, func(i, j int) bool {
        a := strconv.Itoa(points[i].val)
        b := strconv.Itoa(points[j].val)
        sumA, _ := strconv.Atoi(a)
        sumB, _ := strconv.Atoi(b)
        if sumA == sumB {
            return points[i].orig < points[j].orig
        }
        return sumA < sumB
    })
    result := make([]int, len(points))
    for i, point := range points {
        result[i] = point.val
    }
    return result
}