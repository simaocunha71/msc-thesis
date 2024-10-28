func SortArray(arr []int) []int {
    // Create a map to store the number of ones for each number
    onesCount := make(map[int]int)

    // Iterate through the array and count the number of ones for each number
    for _, num := range arr {
        count := 0
        for num != 0 {
            if num&1 == 1 {
                count++
            }
            num >>= 1
        }
        onesCount[num] = count
    }

    // Sort the array based on the number of ones and then the decimal value
    sort.Slice(arr, func(i, j int) bool {
        if onesCount[arr[i]] == onesCount[arr[j]] {
            return arr[i] < arr[j]
        }
        return onesCount[arr[i]] < onesCount[arr[j]]
    })

    return arr
}

