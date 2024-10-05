    coords := make([][2]int, 0)

    for row, innerList := range lst {
        for col, value := range innerList {
            if value == x {
                coords = append(coords, [2]int{row, col})
            }
        }
    }

    sort.Slice(coords, func(i, j int) bool {
        if coords[i][0] == coords[j][0] {
            return coords[i][1] > coords[j][1]
        }
        return coords[i][0] < coords[j][0]
    })

    return coords
}



