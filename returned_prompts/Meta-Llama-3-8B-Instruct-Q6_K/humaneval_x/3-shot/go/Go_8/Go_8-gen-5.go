    sum := 0
    product := 1
    for _, n := range numbers {
        sum += n
        product *= n
    }
    return [2]int{sum, product}
} // This function returns a tuple of sum and product. If you want to return a struct, you can use the following code:
type Result struct {
    Sum int
    Product int
}

func SumProduct(numbers []int) Result {
    sum := 0
    product := 1
    for _, n := range numbers {
        sum += n
        product *= n
    }
    return Result{sum, product}
}