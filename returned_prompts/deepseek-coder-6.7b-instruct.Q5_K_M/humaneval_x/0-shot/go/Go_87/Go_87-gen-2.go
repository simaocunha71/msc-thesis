    var result [][2]int

    for i, row := range lst {
        for j, value := range row {
            if value == x {
                result = append(result, [2]int{i, j})