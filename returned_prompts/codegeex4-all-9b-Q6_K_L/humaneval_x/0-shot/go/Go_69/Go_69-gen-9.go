func Search(lst []int) int {
    freq := map[int]int{}
    for _, v := range lst {
        freq[v]++
    }
    maxFreq := 0
    for k, v := range freq {
        if v >= k && v > maxFreq {
            maxFreq = v
        }
    }
    for k, v := range freq {
        if v == maxFreq && k > maxFreq {
            return k
        }
    }
    return -1
}