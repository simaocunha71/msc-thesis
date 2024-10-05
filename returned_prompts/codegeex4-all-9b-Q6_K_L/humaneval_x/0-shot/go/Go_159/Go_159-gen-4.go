func Eat(number, need, remaining int) []int {
    eaten := number + need
    if eaten > remaining {
        eaten = remaining
    }
    return []int{eaten, remaining - eaten}
}