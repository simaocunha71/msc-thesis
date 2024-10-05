func SumProduct(numbers []int) [2]int {
    var sum, product int
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}