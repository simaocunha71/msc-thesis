
    // Initializing a count variable to 0
    count := 0

    // Loop through the string
    for i := 0; i < len(str) - len(substring) + 1; i++ {
        // If the substring is found in the string
        if str[i:i+len(substring)] == substring {
            // Increment the count
            count++
        }
    }
    // Return the count
    return count
}

*/

func HowManyTimes(str string, substring string) int {
	count := 0
	for i := 0; i < len(str)-len(substring)+1; i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}

// Run test
func main() {
	fmt.Println(HowManyTimes("", "a"))        // 0
	fmt.Println(HowManyTimes("aaa", "a"))     // 3
	fmt.Println(HowManyTimes("aaaa", "aa"))   // 3
	fmt.Println(HowManyTimes("banana", "na")) // 2
}

// Output: 0 3 3 2
// This means that the substring "a" was found 3 times, "aa" was found 3 times, "na" was found 2 times, and an empty string was found 0 times.
// Please note that the function counts overlapping cases too, since it compares the substring with the sections of the string that are of the same length as the substring.
// For example, in the string "aaaa", the substring "aa" is found 3 times (2 non-overlapping times and 1 overlapping time).
// In the string "banana", the substring "na" is found 2 times (2 non-overlapping times).
