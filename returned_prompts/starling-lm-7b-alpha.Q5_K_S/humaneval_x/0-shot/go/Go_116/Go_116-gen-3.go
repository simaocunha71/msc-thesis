    type Pair struct {
        val  int
        ones int
    }

    pairs := []Pair{}
    for _, v := range arr {
        pairs = append(pairs, Pair{v, countOnes(v)})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].ones < pairs[j].ones
    })

    result := []int{}
    for _, v := range pairs {
        result = append(result, v.val)
    }
    return result
}

func countOnes(v int) int {
    count := 0
    for ; v > 0; v >>= 1 {
        if v%2 == 1 {
            count++
        }
    }
    return count
}





In this Kata, you have to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. For similar number of ones, sort based on decimal value. It must be implemented like this: >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5] >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2] >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]

In the implementation, a slice of Pair is used to store each value and the number of ones in its binary representation. The SortArray function sorts the slice of Pair in ascending order. The result is obtained by extracting the values from the slice of Pair.

Here is a detailed explanation of the solution:

1. Create an empty slice of Pair to store each value and the number of ones in its binary representation.
2. Iterate over the input array and append Pair to the slice of Pair, where each Pair has a value and the number of ones in its binary