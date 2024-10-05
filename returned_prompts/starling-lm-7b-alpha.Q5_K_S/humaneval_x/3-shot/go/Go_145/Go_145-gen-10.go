    type point struct {
        num   int
        index int
    }
    result := make([]int, 0)
    points := make([]point, 0)
    for i, n := range nums {
        points = append(points, point{n, i})
    }
    sort.Slice(points, func(i, j int) bool {
        i_sum := 0
        j_sum := 0
        for _, c := range strconv.Itoa(points[i].num) {
            i_sum += int(c - '0')
        }
        for _, c := range strconv.Itoa(points[j].num) {
            j_sum += int(c - '0')
        }
        if i_sum == j_sum {
            return points[i].index < points[j].index
        } else {
            return i_sum < j_sum
        }
    })
    for _, p := range points {
        result = append(result, p.num)
    }
    return result
}



