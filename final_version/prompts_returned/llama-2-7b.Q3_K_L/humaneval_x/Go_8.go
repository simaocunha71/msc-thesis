
// For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
// Empty sum should be equal to 0 and empty product should be equal to 1.
// >>> SumProduct([])
// (0, 1)
// >>> SumProduct([1, 2, 3, 4])
// (10, 24)
func SumProduct(numbers []int) [2]int {
    var sum = 0
    var product = 1
    for _, element := range numbers {
        product *= element
        sum += element
    }
    return [2]int{sum, product}
}

// SumProduct is function that computes a tuple consisting of sum and product of all the integers in a list.
func SumProduct(numbers []int) [2]int {
    sum := 0
    product := 1
    for _, element := range numbers {
        sum += element
        product *= element
    }
    return [2]int{sum, product}
}

// SumProduct is function that computes a tuple consisting of sum and product of all the integers in a list.
func SumProduct(numbers []int) (int, int){
    for _, element := range numbers {
        if element == 0 {
            return element*element, element
        }
    }
}

// SumProduct is function that computes a tuple consisting of sum and product of all the integers in a list.
func SumProduct(numbers []int) (sum int, prod int){
    for _, element := range numbers {
        if element == 0 {
            return element*element, element
        }
    }
}
