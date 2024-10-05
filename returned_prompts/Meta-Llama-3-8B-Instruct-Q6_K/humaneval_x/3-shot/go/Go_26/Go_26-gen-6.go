    var seen = make(map[int]bool)
    result := make([]int, 0)

    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}  // Time complexity: O(n), Space complexity: O(n)  where n is the number of elements in the input list.