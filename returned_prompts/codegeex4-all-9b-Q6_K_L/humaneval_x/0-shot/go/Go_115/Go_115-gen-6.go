import (
    "math"
)

func MaxFill(grid [][]int, capacity int) int {
    var total int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                total += math.Ceil(float64(capacity) / float64(cell))
            }
        }
    }
    return int(total)
}

func main() {
    grid1 := [][]int{{0, 0, 1, 0}, {0, 1, 0, 0}, {1, 1, 1, 1}}
    bucket_capacity1 := 1
    fmt.Println(MaxFill(grid1, bucket_capacity1)) // Output: 6

    grid2 := [][]int{{0, 0, 1, 1}, {0, 0, 0, 0}, {1, 1, 1, 1}, {0, 1, 1, 1}}
    bucket_capacity2 := 2
    fmt.Println(MaxFill(grid2, bucket_capacity2)) // Output: 5

    grid3 := [][]int{{0, 0, 0}, {0, 0, 0}}
    bucket_capacity3 := 5
    fmt.Println(MaxFill(grid3, bucket_capacity3)) // Output: 0
}

