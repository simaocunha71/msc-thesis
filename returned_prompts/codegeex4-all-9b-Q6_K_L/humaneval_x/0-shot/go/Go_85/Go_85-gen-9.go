func Add(lst []int) int {
    sum := 0
    for i, num := range lst {
        if i % 2 == 1 && num % 2 == 0 {
            sum += num
        }
    }
    return sum
}