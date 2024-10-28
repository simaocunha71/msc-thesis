    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    var (
        left, right, min int
        index            int
    )

    for i := 1; i < len(word)-1; i++ {
        if left == 0 && word[i-1] == '*' {
            left = i - 1
        } else if right == 0 && word[i+1] == '*' {
            right = i + 1
        }
        if left != 0 && right != 0 {
            min = right - left
        } else if left == 0 {
            min = right
        } else if right == 0 {
            min = left
        }
        for _, v := range vowels {
            if word[i] == v {
                index = i
                break
            }
        }
        if min > i-index {
            left = i - 1
            right = i + 1
            min = i - index
        }
    }
    if min == 0 {
        return ""
    }
    return word[index : index+1]
}



























































































































































































































