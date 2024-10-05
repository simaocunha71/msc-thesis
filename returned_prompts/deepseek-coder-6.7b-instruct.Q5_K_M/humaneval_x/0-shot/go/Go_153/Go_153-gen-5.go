    max := math.MinInt32
    strongest := ""
    for _, extension := range extensions {
        cap, sm := count_cap_sm(extension)
        strength := cap - sm
        if strength > max {
            max = strength
            strongest = extension
        }
    }
    return class_name + "." + strongest
}

func count_cap_sm(str string) (cap, sm int) {
    for _, r := range str {
        if unicode.IsUpper(r) {
            cap++
        } else if unicode.IsLower(r) {
            sm++
        }
    }
    return
}

func main() {
    fmt.Println(StrongestExtension("my_class", []string{"AA", "Be", "CC"})) // Output: my_class.AA
}

This solution uses a helper function count_cap_sm() to count the number of uppercase and lowercase letters in the extension, then calculates the strength of the extension and keeps track of the strongest extension.
*/

import (
	"strings"
)

// countCapitalAndSmallLetters counts the number of capital and small letters in the string.
func countCapitalAndSmallLetters(s string) (capital, small int) {
	for _, r := range s {
		if 'A' <= r && r <= 'Z' {
			capital++
		} else if 'a' <= r && r <= 'z' {
			small++
		}
	}
	return
}

// StrongestExtension finds the strongest extension by comparing the strength of each extension.
func StrongestExtension(class_name string, extensions []string) string {
	maxStrength := -1000000
	strongestExtension := ""
	for _, extension := range extensions {
		capital, small := countCapitalAndSmallLetters(extension)
		strength := capital - small
		if strength > maxStrength {
			maxStrength = strength
			strongestExtension = extension
		}
	}
	return class_name + "." + strongestExtension
}

func main() {
	f