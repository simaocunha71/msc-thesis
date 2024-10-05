func SumProduct(numbers []int) [2]int {
    if len(numbers) == 0 {
        return [2]int{0, 1}
    }
    sum := 0
    product := 1
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}