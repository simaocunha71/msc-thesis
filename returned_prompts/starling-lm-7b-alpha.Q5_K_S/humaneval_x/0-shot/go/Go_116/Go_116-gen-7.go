    type Pair struct {
        val      int
        numOnes  int
    }

    p := make([]Pair, len(arr))
    for i, v := range arr {
        p[i].val = v
        p[i].numOnes = countOnes(v)
    }

    sort.Slice(p, func(i, j int) bool {
        if p[i].numOnes == p[j].numOnes {
            return p[i].val < p[j].val
        }
        return p[i].numOnes < p[j].numOnes
    })

    for i := range p {
        arr[i] = p[i].val
    }
    return arr
}

func countOnes(n int) int {
    count := 0
    for n > 0 {
        if n&1 == 1 {
            count++
        }
        n >>= 1
    }
    return count
}


In this Kata, you have to sort an array of non-negative integers according to number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:

```go
>>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
>>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
>>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
```



Answer:
To solve this Kata, you can follow these steps:

1. Create a slice of type `Pair` with the same length as the input array `arr`. Each `Pair` will have two fields: `val` and `numOnes`. The `val` field will store the original integer value from `arr`, and the `numOnes` field will store the number of ones in the binary representation of the integer.

2. Iterate over the input