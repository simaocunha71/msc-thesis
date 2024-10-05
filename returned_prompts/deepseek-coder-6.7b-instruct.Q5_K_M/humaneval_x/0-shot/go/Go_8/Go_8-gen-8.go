
    sum := 0
    product := 1

    for _, num := range numbers {
        sum += num
        product *= num
    }

    return [2]int{sum, product}
}
```

In the above code, we first initialize the variables sum and product to 0 and 1 respectively. Then, we iterate over the numbers array using range. In each iteration, we add the current number to sum and multiply the product by the current number. Finally, we return a tuple containing the sum and product as a [2]int array.

This code should pass all the provided test cases.
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
	fmt.Println(SumProduct([]int{}))        // should print [0 1]
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // should print [10 24]
}

/*
Output:
[0 1]
[10 24]
*/

/*
Explanation:

In the first test case, the function SumProduct is called with an empty array. As a result, sum is 0 and product is 1, so the function returns [0 1].

In the second test case, the function SumProduct is called with an array [1, 2, 3, 4]. As a result, sum is 10 (1+2+3+4) and product is 24 (1*2*3*4), so the function returns [10 24].
*/
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"regexp"
	"strings"
)

func main() {
	resp, err := http.Get("https://www.wikipedia.org/")
