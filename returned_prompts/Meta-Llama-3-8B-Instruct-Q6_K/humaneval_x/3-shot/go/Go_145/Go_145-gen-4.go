    type Point struct {
        val int
        ind int
    }
    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i] = Point{val: num, ind: i}
    }
    sort.Slice(points, func(i, j int) bool {
        sum1, _ := strconv.Atoi(strconv.Itoa(math.Abs(int(points[i].val))).replace("", ""))
        sum2, _ := strconv.Atoi(strconv.Itoa(math.Abs(int(points[j].val))).replace("", ""))
        if sum1 != sum2 {
            return sum1 < sum2
        }
        return points[i].ind < points[j].ind
    })
    result := make([]int, len(points))
    for i, point := range points {
        result[i] = point.val
    }
    return result
}

func (p string) replace(c, r string) string {
    return strings.Replace(p, c, r, -1)
}
}