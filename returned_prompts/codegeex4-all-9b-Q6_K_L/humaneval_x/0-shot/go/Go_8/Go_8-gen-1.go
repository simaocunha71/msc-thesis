The function SumProduct takes a slice of integers as input and returns a tuple consisting of the sum and the product of all the integers in the input slice. 

Here is the implementation in Go:

```go
func SumProduct(numbers []int) [2]int {
    sum := 0
    product := 1

    for _, num := range numbers {
        sum += num
        product *= num
    }

    return [2]int{sum, product}
}
```

The function starts by initializing the sum and product variables to 0 and 1 respectively. Then, it iterates over the input slice using a for loop and adds each number to the sum and multiplies it with the product. Finally, it returns a tuple containing the sum and product.

The time complexity of this function is O(n), where n is the length of the input slice.