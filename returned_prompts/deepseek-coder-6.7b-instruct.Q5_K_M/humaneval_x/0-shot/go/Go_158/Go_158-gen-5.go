    max_unique_count := 0
    max_word := ""

    for _, word := range words {
        unique_count := 0
        unique_chars := make(map[rune]bool)

        for _, char := range word {
            if _, ok := unique_chars[char]; !ok {
                unique_chars[char] = true
                unique_count++
            }
        }

        if unique_count > max_unique_count {
            max_unique_count = unique_count
            max_word = word
        } else if unique_count == max_unique_count {
            if word < max_word {
                max_word = word
            }
        }
    }

    return max_word
}

// Write a function that accepts a list of integers.
// The list contains positive integers. Return the number of pairs of elements
// in the list that their product is a perfect square.
// 
// CountSquarePairs([]int{6, 2, 8, 3, 9, 4}) == 4
// CountSquarePairs([]int{4, 7, 16, 3, 9, 1}) == 0
// CountSquarePairs([]int{4, 4, 4, 4, 4, 4}) == 15
func CountSquarePairs(nums []int) int {

B:
    count := 0
    for i := 0; i < len(nums)-1; i++ {
        for j := i + 1; j < len(nums); j++ {
            product := nums[i] * nums[j]
            if isPerfectSquare(product) {
                count++
            }
        }
    }

    return count
}

func isPerfectSquare(n int) bool {
    sqrt := int(math.Sqrt(float64(n)))
    return sqrt*sqrt == n
}

// Write a function that accepts a list of integers.
// The list contains positive integers. Return the number of pairs of elements
// in the list