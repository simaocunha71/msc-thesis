```
    var sum int
    var product int
    for _, num := range numbers {
        sum += num
        product *= num
    }
    if product == 0 {
        product = 1
    }
    return [2]int{sum, product}
}
```

This solution defines a function `SumProduct` that takes a slice of integers `numbers` as input. It initializes two variables `sum` and `product` to 0 and 1, respectively. Then it iterates over the input slice, adding each number to `sum` and multiplying each number to `product`. If the product becomes 0 during the iteration, it is reset to 1 to avoid division by zero error. Finally, the function returns a tuple of the calculated sum and product. The tuple is of type `[2]int` which is a fixed-size array of two integers. 

This solution is concise and efficient, with a time complexity of O(n) where n is the length of the input slice. It also handles the edge case where the input slice is empty, returning a tuple of (0, 1) as required. 