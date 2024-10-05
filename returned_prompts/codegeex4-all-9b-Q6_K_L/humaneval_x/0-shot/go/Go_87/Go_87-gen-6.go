func GetRow(lst [][]int, x int) [][2]int {
    var arr [][2]int

    for i, row := range lst {
        for j, v := range row {
            if v == x {
                arr = append(arr, [2]int{i, j})
            }
        }
    }

    sort.Slice(arr, func(i, j int) bool {
        if arr[i][0] == arr[j][0] {
            return arr[i][1] > arr[j][1]
        }
        return arr[i][0] < arr[j][0]
    })

    return arr
}
