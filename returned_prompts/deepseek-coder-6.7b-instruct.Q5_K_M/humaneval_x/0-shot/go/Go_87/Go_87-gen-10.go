    var coordinates [][2]int
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                coordinates = append(coordinates, [2]int{i