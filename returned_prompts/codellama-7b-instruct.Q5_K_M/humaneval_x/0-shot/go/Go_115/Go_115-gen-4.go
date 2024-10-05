    for i, r := range grid {
        for j, v := range r {
            if v == 1 {
                for k := 0; k < capacity; k++ {
                    if j+k < len(r) {
                        r[j+k] = 0
                    } else {
                        r[j] = 0
                        continue A
                    }
                }
            }
        }
    }

    return len(grid)
}

func main() {
    grid := [][]int{
        {0, 0, 1, 0},
        {0, 1, 0, 0},
        {1, 1, 1, 1},
    }

    capacity := 1

    fmt.Println(MaxFill(grid, capacity))
}
