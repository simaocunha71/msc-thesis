func Solution(lst []int) int {
    var sum int
    for i, num := range lst {
        if i % 2 == 0 && num % 2 != 0 {
            sum += num
        }
    }
    return sum
}