    sort.Slice(arr, func(i, j int) bool {
        n1, n2 := arr[i], arr[j]
        c1, c2 := countOnes(n1), countOnes(n2)

        if c1 == c2 {
            return n1 < n2
        }
        return c1 < c2
    })
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

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4})) // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6})) // [-6, -5, -4, -3, -2]
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4})) // [0, 1, 2, 3, 4]
}

