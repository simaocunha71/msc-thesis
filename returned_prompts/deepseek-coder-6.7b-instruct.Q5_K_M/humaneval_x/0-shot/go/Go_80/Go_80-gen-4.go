
	if len(s) < 3 {
		return false
	}

	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(IsHappy("a"))       // false
	fmt.Println(IsHappy("aa"))      // false
	fmt.Println(IsHappy("abcd"))    // true
	fmt.Println(IsHappy("aabb"))    // false
	fmt.Println(IsHappy("adb"))     // true
	fmt.Println(IsHappy("xyy"))     // false
	fmt.Println(IsHappy("aabba"))    // false
	fmt.Println(IsHappy("adbba"))   // false
	fmt.Println(IsHappy("abcb"))    // false
	fmt.Println(IsHappy("aabbcb"))  // false
	fmt.Println(IsHappy("abc"))     // true
}


// The time complexity of this solution is O(n) and the space complexity is O(1), where n is the length of the string.
// The solution iterates through the string only once and checks the conditions at each step.
// Therefore, it is a linear time solution.
// The space complexity is constant because it does not use any additional space that scales with the size of the input.
// The solution works for all strings, as it checks if every 3 consecutive letters are distinct.
// If the string is less than 3 characters long, it returns false.
// If any 3 consecutive letters are the same, it returns false.
// If all conditions are met, it returns true.
// This solution assumes that the input string is only composed of lowercase letters.
// If the input string can contain uppercase letters or special characters, the solution would need to be adjusted accordingly.
// Also, the solution does not handle non-string inputs. If this is a possibility, additional error checking should be added.
// Additionally, if the string contains non-letter characters, the solution