    var ret [][]int

    for i, row := range lst {
        if len(row) > 0 {
            for j := len(row) - 1; j >= 0; j-- {
                if row[j] == x {
                    ret = append(ret, []int{i, j})
                }
            }
        }
    }

    sort.Slice(ret, func(i, j int) bool {
        return ret[i][0] < ret[j][0]
    })

    for i := range ret {
        sort.Slice(ret[i], func(i, j int) bool {
            return ret[i][1] > ret[j][1]
        })
    }

    return ret
}

go run main.go

func main() {
    GetRow([][]int{
        {},
        {},
        {1, 2, 3, 4, 5, 6},
        {1, 2, 3, 4, 1, 6},
        {1, 2, 3, 4, 5, 1},
    }, 1)
}








































































































































































































































