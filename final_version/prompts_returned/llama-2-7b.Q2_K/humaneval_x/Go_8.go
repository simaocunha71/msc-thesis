
// For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
// Empty sum should be equal to 0 and empty product should be equal to 1.
// >>> SumProduct([])
// (0, 1)
// >>> SumProduct([1, 2, 3, 4])
// (10, 24)
func SumProduct(numbers []int) [2]int {
    var prod = 1
    for _, n := range numbers {
        prod *= n
        sum = sum + n
    }
    return [2]int{sum: sum, product: prod}
}