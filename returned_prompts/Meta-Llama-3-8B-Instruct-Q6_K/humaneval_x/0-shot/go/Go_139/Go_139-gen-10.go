// Start of your solution
if n <= 1 {
    return 1
}

result := 1
for i := n; i > 1; i-- {
    result *= int(math.Pow(float64(i), float64(n-i+1)))
}
return int(result)
}

package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(SpecialFactorial(4))  // Output: 288
	fmt.Println(SpecialFactorial(5))  // Output: 34560
}

