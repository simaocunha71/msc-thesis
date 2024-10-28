    type point struct {
        number int
        index  int
    }

    points := make([]point, 0, len(nums))
    for i, n := range nums {
        points = append(points, point{
            number: n,
            index:  i,
        })
    }

    sort.Slice(points, func(i, j int) bool {
        i_sum, j_sum := 0, 0
        for _, c := range strconv.Itoa(points[i].number) {
            if c >= '0' && c <= '9' {
                i_sum += int(c - '0')
            }
        }
        for _, c := range strconv.Itoa(points[j].number) {
            if c >= '0' && c <= '9' {
                j_sum += int(c - '0')
            }
        }
        if i_sum != j_sum {
            return i_sum < j_sum
        }
        return points[i].index < points[j].index
    })

    result := make([]int, 0, len(nums))
    for _, point := range points {
        result = append(result, point.number)
    }
    return result
}



