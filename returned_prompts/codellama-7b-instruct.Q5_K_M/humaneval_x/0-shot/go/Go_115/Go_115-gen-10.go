    for _, row := range grid {
        for _, col := range row {
            if col == 0 {
                continue A
            }
        }
    }

    return 0
}

func MaxFill2(grid [][]int, capacity int) int {
    var (
        max_fill int
        max_fill_row int
    )
    for i := 0; i < len(grid); i++ {
        max_fill = 0
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] > max_fill {
                max_fill = grid[i][j]
                max_fill_row = i
            }
        }
    }
    //fmt.Println(max_fill, max_fill_row)

    for i := 0; i < len(grid); i++ {
        if i == max_fill_row {
            continue
        }
        if grid[i][0] > max_fill {
            max_fill = grid[i][0]
        }
    }

    return max_fill
}

// 2019-07-25
// https://leetcode.com/problems/minimum-number-of-refuelings/

func MinRefuel(target int, startFuel int, stations [][]int) int {
	var (
		ans, totalFuel int
	)
	for i := 0; i < len(stations); i++ {
		startFuel -= totalFuel
		totalFuel += stations[i][0]
		if startFuel >= stations[i][1] {
			continue
		}
		ans++
		startFuel = stations[i][1] - startFuel
		totalFuel += startFuel
	}
	startFuel -= totalFuel
	if startFuel < target {
		ans++
	}
	return ans
}

// 2019-07-23
// https://leetcode.com/problems/maximum-area-of-a-piece