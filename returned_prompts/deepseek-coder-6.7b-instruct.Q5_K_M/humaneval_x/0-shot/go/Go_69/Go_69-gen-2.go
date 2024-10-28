
    // First we need to count the frequency of each number in the list
    freq := make(map[int]int)
    for _, num := range lst {
        freq[num]++
    }

    // Then we iterate over the list in reverse order
    for i := len(lst) - 1; i >= 0; i-- {
        // If the frequency of the current number is greater than or equal to its value
        if freq[lst[i]] >= lst[i] {
            // Return the number
            return lst[i]
        }
    }

    // If no such number was found, return -1
    return -1
}

// The time complexity of this solution is O(n) because we are iterating over the list twice. The space complexity is O(n) as well because we are using a dictionary to store the frequencies.

// If the input list is sorted in descending order, we can optimize this solution by iterating over the list once. This will reduce the time complexity to O(n).

func Search(lst  []int) int  {
    freq := make(map[int]int)
    for _, num := range lst {
        freq[num]++
        if freq[num] >= num {
            return num
        }
    }
    return -1
}

// This optimized solution has the same space complexity O(n) but the time complexity is reduced to O(n).
// Please note that the time complexity of this optimized solution depends on the order of the input list. If the input list is already sorted in descending order, the time complexity will be O(n), otherwise, it will be O(n log n) due to the sorting operation.

// This solution assumes that the input list contains only positive integers. If the input list contains negative integers, this solution may not work correctly.
// In such a case, we would need to adjust the solution to handle negative integers by using a different data structure to store the frequencies.
// For example, we could use an array of size equal to the maximum value in the list to store the frequencies.
// This adjustment would increase the space complexity but would not affect the time complexity.
*/