    sort.Slice(arr, func(i, j int) bool {
        // For each pair of elements, count the number of ones in their binary
        // representation.
        countI := countOnes(arr[i])
        countJ := countOnes(arr[j])
        // If the counts are equal, sort based on the decimal values of the
        // elements. Otherwise, sort based on the counts.
        if countI == countJ {
            return arr[i] < arr[j]
        }
        return countI < countJ
    })
    return arr
}

func countOnes(n int) (count int) {
    for n != 0 {
        n = n & (n - 1)
        count++
    }
    return count
}






func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        return bits.OnesCount(uint(arr[i])) < bits.OnesCount(uint(arr[j])) || 
               (bits.OnesCount(uint(arr[i])) == bits.OnesCount(uint(arr[j])) && arr[i] < arr[j])
    })
    return arr
}





func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        x, y := arr[i], arr[j]
        cx, cy := 0, 0
        for x > 0 {
            if x & 1 == 1 {
                cx++
            }
            x >>= 1
        }
        for y > 0 {
            if y & 1 == 1 {
                cy++
            }
            y >>= 1
        }
        return cx < cy || (cx == cy && arr[i] < arr[j])
    })
    return arr
}






func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        x, y := arr[i], arr[j]
       