    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, char := range txt {
            if unicode.IsLower(char) && int(char-'a') % 2 != 0 {
                count++
            }
        }
        return count
    }
}

func main() {
    fmt.Println(SplitWords("Hello world!"))
    fmt.Println(SplitWords("Hello,world!"))
    fmt.Println(SplitWords("abcdef"))
}

*/

import (
	"strings"
	"unicode"
)

func SplitWords(txt string) interface{} {
	if strings.Contains(txt, " ") {
		return strings.Split(txt, " ")
	} else if strings.Contains(txt, ",") {
		return strings.Split(txt, ",")
	} else {
		count := 0
		for _, char := range txt {
			if unicode.IsLower(char) && int(char-'a')%2 != 0 {
				count++
			}
		}
		return count
	}
}

// This is a way to solve the problem
func main() {
	fmt.Println(SplitWords("Hello world!"))
	fmt.Println(SplitWords("Hello,world!"))
	fmt.Println(SplitWords("abcdef"))
}

/*
The SplitWords function checks if the string contains any white space or comma.
If it contains a white space it splits the string at those points and returns the split words as a list.
If it contains a comma it also splits the string at the comma and returns the split words as a list.
If it does not contain any white spaces or commas, it counts the number of lowercase letters with an odd order in the alphabet
and returns that count.
*/

// This is a way to solve the problem
func main() {
	fmt.Println(SplitWords("Hello world!"