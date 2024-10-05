
  if n%2 == 1 {
    return false
  }

  for i := 2; i < n/2; i += 2 {
    for j := 2; j < n/2; j += 2 {
      for k := 2; k < n/2; k += 2 {
        for l := 2; l < n/2; l += 2 {
          if i + j + k + l == n {
            return true
          }
        }
      }
    }
  }

  return false

}

func main()  {
  fmt.Println(IsEqualToSumEven(4))
  fmt.Println(IsEqualToSumEven(6))
  fmt.Println(IsEqualToSumEven(8))
}
```

This solution is not efficient and it's not the best way to solve this problem. We will get the time complexity O(n^4) which is not feasible for large inputs of n.

A more efficient solution will be to check the remainder of n divided by 4. If n is divisible by 4, then n can be written as the sum of 4 positive even numbers.

Here is the optimized code in Golang:

```golang
package main

import "fmt"

func IsEqualToSumFourEven(n int) bool {
  return n%4 == 0
}

func main()  {
  fmt.Println(IsEqualToSumFourEven(4))
  fmt.Println(IsEqualToSumFourEven(6))
  fmt.Println(IsEqualToSumFourEven(8))
}
```

This solution is more efficient and will run in constant time O(1).

Note: This solution assumes that n is a positive integer and it does not take into account the case where n is negative or zero.

This solution is based on the fact that if n is an even number, it can be written as the sum of 4 even numbers, each of which is 2. So if n is divisible by 4, it can be written as the sum of 4 even numbers. If n is not divisible by 4, it cannot be written as the sum of 4 even numbers.
