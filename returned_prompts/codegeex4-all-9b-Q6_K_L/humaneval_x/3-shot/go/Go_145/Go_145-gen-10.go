    points := make([][]int,0)
    for i, n := range nums{
        p := make([]int,0)
        p = append(p,i)
        p = append(p,n)
        points = append(points,p)
    }

    sort.Slice(points, func(i, j int) bool {
        iSum := 0
        for _, c := range strconv.Itoa(points[i][1]){
            iSum += int(c-'0')
        }

        jSum := 0
        for _, c := range strconv.Itoa(points[j][1]){
            jSum += int(c-'0')
        }

        return iSum < jSum
    })

    result := make([]int,0)
    for _, p := range points{
        result = append(result,p[1])
    }

    return result
}