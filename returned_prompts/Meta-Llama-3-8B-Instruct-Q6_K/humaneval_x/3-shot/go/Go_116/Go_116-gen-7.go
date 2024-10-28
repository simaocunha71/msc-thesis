    type pair struct {
        num int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        p1 := pair{arr[i], binToInt(binToDec(arr[i]))}
        p2 := pair{arr[j], binToInt(binToDec(arr[j]))}
        if p1.ones != p2.ones {
            return p1.ones < p2.ones
        }
        return p1.num < p2.num
    })

    return arr
}

func binToDec(n int) string {
    return fmt.Sprintf("%b", n)
}

func binToInt(s string) int {
    n, _ := strconv.ParseInt(s, 2, 64)
    return int(n)
}