```go
package main

import (
	"fmt"
)

func IsEqualToSumEven(n int) bool {
	for a := 2; a <= n; a += 2 {
		for b := 2; b <= n-a; b += 2 {
			for c := 2; c <= n-a-b; c += 2 {
				for d := 2; d <= n-a-b-c; d += 2 {
					if a+b+c+d == n {
						return true
					}
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println(IsEqualToSumEven(4)) // false
	fmt.Println(IsEqualToSumEven(6)) // false
	fmt.Println(IsEqualToSumEven(8)) // true
}
```

Explanation:
The function `IsEqualToSumEven(n int) bool` checks whether the given number `n` can be written as the sum of exactly 4 positive even numbers. It uses four nested loops to iterate through all possible combinations of even numbers that sum up to `n`. If it finds a combination that sums up to `n`, it returns `true`. If it doesn't find any such combination after checking all possible combinations, it returns `false`. The function is tested in the `main` function with examples of 4, 6, and 8. The output is printed to the console. 

Note: The function may take a long time to execute for large values of `n` because it checks all possible combinations of even numbers. For a more efficient solution, you may need to use a more advanced algorithm or data structure. 

For example, you could use a recursive function to check if the sum of 4 even numbers equals `n`, or you could use a hash table to store the sums of even numbers and check if `n` is in the hash table. These approaches would be more efficient than the brute force approach used in this function. 

Here is an example of a recursive function that checks if the sum of 4 even numbers equals `n`:

```go
func IsEqualToSumEven(n int) bool {
	if n < 8 {
		return false
	}
	return checkSum(n, 0, 0, 0, 0)
}

func checkSum(n int, a, b, c, d int) bool {
	if a+b+c+d == n {
		return true
	}
	if a+b+c+d > n {
		return false