    words := strings.Fields(test)
    count := make(map[rune]int)
    max := 0

B:
    for _, word := range words {
        for _, char := range word {
            count[char]++
            if count[char] > max {
                max = count[char]
            }
        }
    }

C:
    res := make(map[rune]int)
    for k, v := range count {
        if v == max {
            res[k] = v
        }
    }

    return res
}


A: Split the string into a slice of words using strings.Fields().

B: Count the occurrence of each character in the words and update the maximum occurrence.

C: Create a new map with the character and its count if its count is equal to the maximum.

