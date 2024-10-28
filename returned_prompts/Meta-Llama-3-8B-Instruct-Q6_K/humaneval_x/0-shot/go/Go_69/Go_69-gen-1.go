The problem can be solved by iterating over the list and keeping track of the maximum frequency and the corresponding number. Here is a possible implementation in Go:
```go
func Search(lst []int) int {
    freq := make(map[int]int)
    maxFreq := 0
    maxNum := -1

    for _, num := range lst {
        if _, ok := freq[num]; ok {
            freq[num]++
        } else {
            freq[num] = 1
        }
        if freq[num] >= num && num > 0 {
            if freq[num] > maxFreq {
                maxFreq = freq[num]
                maxNum = num
            }
        }
    }
    if maxNum == -1 {
        return -1
    }
    return maxNum
}
```
Here's an explanation of the code:

1. We create a map `freq` to store the frequency of each number in the list.
2. We initialize `maxFreq` to 0 and `maxNum` to -1.
3. We iterate over the list using a range loop.
4. For each number, we increment its frequency in the `freq` map. If the number is not present in the map, we set its frequency to 1.
5. We check if the frequency of the current number is greater than or equal to the number itself and if the number is greater than 0. If both conditions are true, we update `maxFreq` and `maxNum` if the current frequency is greater than the previous maximum frequency.
6. If `maxNum` is still -1 after iterating over the entire list, we return -1. Otherwise, we return `maxNum`.

You can test this function with the examples provided in the problem statement to verify its correctness.