
// ... your code here

}

// Here is a possible solution in Go:

package kata

func Tri(n int) []float64 {
  arr := make([]float64, n+1)
  arr[0] = 3
  if n > 0 {
    arr[1] = 2
  }
  if n > 1 {
    arr[2] = 8
  }
  for i := 3; i <= n; i++ {
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
  }
  return arr
}

// This solution uses the standard dynamic programming approach. It initializes the first few elements of the array with the first few elements of the Tribonacci sequence. Then it iterates over the rest of the array and fills it with the sum of the previous three elements. The result is the first n+1 elements of the Tribonacci sequence.

```

**[⬆ Back to Top](#table-of-contents)**

## 40. <a name='40'></a>Hex to Decimal Converter

