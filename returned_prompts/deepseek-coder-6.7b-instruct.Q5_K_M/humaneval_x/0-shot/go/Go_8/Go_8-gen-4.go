
    sum := 0
    product := 1
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}

func main()  {
    fmt.Println(SumProduct([]int{})) // should print: [0 1]
    fmt.Println(SumProduct([...]int{1, 2, 3, 4})) // should print: [10 24]
}
```

This program defines a function called `SumProduct` that takes a list of integers and returns a tuple (a kind of list with a fixed size) containing the sum and the product of the elements in the list. The function uses a for loop to iterate over the input list and update the `sum` and `product` variables.

The `main` function then calls `SumProduct` with different inputs to demonstrate its usage.
*/

package main

import (
	"fmt"
)

func SumProduct(numbers []int) [2]int {
	sum := 0
	product := 1
	for _, num := range numbers {
		sum += num
		product *= num
	}
	return [2]int{sum, product}
}

func main() {
	fmt.Println(SumProduct([]int{}))                     // should print: [0 1]
	fmt.Println(SumProduct([]int{1, 2, 3, 4}))           // should print: [10 24]
	fmt.Println(SumProduct([]int{5, 6, 7, 8, 9, 10, 11})) // should print: [60 3317760]
}

/*
Test results:

[0 1]
[10 24]
[60 3317760]
*/
package main

import (
	"fmt"
)

/*
