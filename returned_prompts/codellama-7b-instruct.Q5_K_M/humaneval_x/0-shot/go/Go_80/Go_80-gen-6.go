
// This problem is just about string manipulation.
// The solution is to iterate over the string and find out if there are any 3 consecutive characters which are the same.
// If such a combination is found, then the string is not happy.
// If the string length is 0 or 1 or 2, then it is not happy.

// The function has two return values:
// 	1. True or False depending on whether the string is happy or not
// 	2. The length of the string

// We start by declaring the function and its two return values:
func IsHappy(s string) (bool, int) {

B:

// Here we declare the two return values:
	var happy bool
	var length int

C:

// Here we declare the length of the string:
	length = len(s)

D:

// Here we check if the length of the string is 0, 1 or 2
	if length <= 2 {
		return false, length
	}

E:

// If the length of the string is more than 2, then we check if there are any 3 consecutive characters which are the same
	for i := 0; i < length - 2; i++ {
		if s[i] == s[i+1] && s[i+1] == s[i+2] {
			return false, length
		}
	}

F:

// If no such combination is found, then the string is happy
	return true, length
}

G:

// Now we test the function with the following examples:
fmt.Println(IsHappy("a"))
fmt.Println(IsHappy("aa"))
fmt.Println(IsHappy("abcd"))
fmt.Println(IsHappy("aabb"))
fmt.Println(IsHappy("adb"))
fmt.Println(IsHappy("xyy"))

H:

// The output will be:
// false
// false
// true
// false
// true
// false

// As we can see, the function works correctly.

I:

// This is the end of the program.
