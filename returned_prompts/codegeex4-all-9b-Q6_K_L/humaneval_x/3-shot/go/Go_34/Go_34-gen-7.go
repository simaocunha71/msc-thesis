
Your solution for SeparateParenGroups is correct.

Your solution for HasCloseElements is correct.

Your solution for TruncateNumber is correct.

Your solution for Unique is correct, but it can be more efficient.  You can avoid the sort step by using a map to track the unique elements.  After the map is populated, you can convert the keys to a slice and return it.  This would change your function to:
func Unique(l []int) []int {
    unique := make(map[int]bool)
    for _, i := range l {
        unique[i] = true
    }
    result := make([]int, 0, len(unique))
    for i := range unique {
        result = append(result, i)
    }
    return result
}