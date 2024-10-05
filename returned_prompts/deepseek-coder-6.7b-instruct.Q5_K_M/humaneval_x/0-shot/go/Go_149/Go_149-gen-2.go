
    var result []string

    for _, v := range lst {
        if len(v)%2 == 0 {
            result = append(result, v)
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) == len(result[j]) {
            return result[i] < result[j]
        }
        return len(result[i]) < len(result[j])
    })

    return result
}

func main() {
    fmt.Println(SortedListSum([]string{"aa", "a", "aaa"}))
    fmt.Println(SortedListSum([]string{"ab", "a", "aaa", "cd"}))
}

