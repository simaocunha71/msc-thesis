    type point struct {
        val int
        idx int
    }
    points := make([]point, len(nums))
    for i, num := range nums {
        points[i].val = num
        points[i].idx = i
    }
    sort.Slice(points, func(i, j int) bool {
        if points[i].val+strconv.Itoa(points[i].val).calcSum() != points[j].val+strconv.Itoa(points[j].val).calcSum() {
            return points[i].val+strconv.Itoa(points[i].val).calcSum() < points[j].val+strconv.Itoa(points[j].val).calcSum()
        }
        return points[i].idx < points[j].idx
    })
    result := make([]int, len(points))
    for i, p := range points {
        result[i] = p.val
    }
    return result
}

func (s string) calcSum() int {
    sum := 0
    for _, c := range s {
        sum += int(c - '0')
    }
    return sum
}