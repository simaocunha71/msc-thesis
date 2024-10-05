    // total number of wells
    var total int
    // total number of buckets
    var buckets int

    // loop over grid rows
    for _, row := range grid {
        // loop over each well in row
        for _, well := range row {
            // increment total if well is full
            total += well
        }
    }

    // calculate number of buckets needed
    buckets = total / capacity
    if total % capacity != 0 {
        // increment buckets if there is a remainder
        buckets++
    }

    return buckets
}

func main() {
    fmt.Println(MaxFill([][]int{{0,0,1,0}, {0,1,0,0}, {1,1,1,1}}, 1)) // should return 6
    fmt.Println(MaxFill([][]int{{0,0,1,1}, {0,0,0,0}, {1,1,1,1}, {0,1,1,1}}, 2)) // should return 5
    fmt.Println(MaxFill([][]int{{0,0,0}, {0,0,0}}, 5)) // should