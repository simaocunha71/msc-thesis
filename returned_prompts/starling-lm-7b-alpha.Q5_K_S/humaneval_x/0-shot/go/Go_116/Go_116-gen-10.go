    for _, v := range arr {
        if v < 0 {
            v = -v
        }
    }
    m := make(map[int]int)
    for _, v := range arr {
        bits := 0
        for {
            if v%2 == 1 {
                bits++
            }
            v /= 2
            if v == 0 {
                break
            }
        }
        m[bits]++
    }
    s := make([]int, 0, len(m))
    for k, v := range m {
        for i := 0; i < v; i++ {
            s = append(s, k)
        }
    }
    sort.Slice(s, func(i int, j int) bool {
        return s[i]+s[j] < s[j]+s[i]
    })
    return s


Answer & Explanation:
In this kata, you need to sort an array of non-negative integers according to the number of ones in the binary representation of the integer in ascending order. For the same number of ones, you need to sort by the decimal value.

To solve this problem, we can follow these steps:

1. Initialize an empty map `m` to store the count of integers with a specific number of ones in their binary representation.
2. Iterate through each integer in the input array `arr`. For negative integers, make them positive by taking their absolute value.
3. For each integer, calculate the number of ones in its binary representation using a while loop. Increment the count of ones in the map `m` if the integer has a one at the current bit position. If the integer has a zero at the current bit position, continue to the next bit.
4. After iterating through all the integers, initialize an empty slice `s` to store the integers with their corresponding number of ones.
5. Iterate through the map `m` in ascending order of the number of ones. For each number of ones, append the corresponding integer to the slice `s` the same number of times as its count in the map.
6. Use the `sort.Slice` function to sort the slice `s` in ascending order based