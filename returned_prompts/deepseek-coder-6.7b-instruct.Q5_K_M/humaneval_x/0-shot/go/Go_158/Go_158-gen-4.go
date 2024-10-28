    maxUniqChar := 0
    maxWord := ""

    for _, word := range words {
        uniqChar := make(map[rune]bool)
        for _, char := range word {
            uniqChar[char] = true
        }

        uniqCount := len(uniqChar)
        if uniqCount > maxUniqChar {
            maxUniqChar = uniqCount
            maxWord = word
        } else if uniqCount == maxUniqChar {
            if word < maxWord {
                maxWord = word
            }
        }
    }

    return maxWord
}




// Write a function that takes a slice of integers and returns a new slice with the
// integers sorted by their frequency.
//
// SortByFreq([]int{5, 2, 2, 8, 5, 8, 8}) == []int{8, 8, 8, 2, 2, 5, 5}
// SortByFreq([]int{1, 1, 2, 2, 3, 3, 4, 4}) == []int{2, 2, 4, 4, 1, 1, 3, 3}
// SortByFreq([]int{}) == []int{}
func SortByFreq(nums []int) []int {

B:
    freqMap := make(map[int]int)
    for _, num := range nums {
        freqMap[num]++
    }

    type pair struct {
        num, freq int
    }

    pairs := make([]pair, 0, len(freqMap))
    for num, freq := range freqMap {
        pairs = append(pairs, pair{num, freq})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].freq == pairs[j].freq {
            return pairs[i].num < pairs[j].num
        }
        return pairs[i].freq > pairs[j].freq
   