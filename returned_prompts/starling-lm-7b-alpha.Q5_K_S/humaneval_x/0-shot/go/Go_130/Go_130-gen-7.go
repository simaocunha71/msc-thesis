
var res []float64 = make([]float64, n + 1)
res[0] = 1
res[1] = 3
res[2] = 2

for i := 3; i < n + 1; i++ {
    if i%2 == 1 {
        res[i] = res[i-1] + res[i-2] + res[i-3] + res[i-4] + res[i-5]
    } else {
        res[i] = res[i-1] + res[i-2] + res[i-3] + res[i-4]
    }
}

return res

*/

```

```
func Tri(n int) []float64 {
    res := make([]float64, n+1)
    res[0] = 1
    res[1] = 3
    res[2] = 2

    for i := 3; i < n+1; i++ {
        if i%2 == 1 {
            res[i] = res[i-1] + res[i-2] + res[i-3] + res[i-4] + res[i-5]
        } else {
            res[i] = res[i-1] + res[i-2] + res[i-3] + res[i-4]
        }
    }

    return res
}
```

In the above code, we initialize a slice of float64 called `res` with the first 3 numbers of the Tribonacci sequence. Then, we loop through the indices from 3 to `n+1` (inclusive), and for every odd index, we calculate the Tribonacci number by adding the previous 5 numbers in the sequence. For every even index, we calculate the Tribonacci number by adding the previous 4 numbers in the sequence. Finally, we return the `res` slice, which contains the first `n+1` numbers of the Tribonacci sequence.

Note: The time complexity of this solution is O(n), as we only need to calculate each Tribonacci number once.

```

```

