func Solution(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i % 2 == 0 && v % 2 == 1 {
            sum += v
        }
    }
    return sum
}