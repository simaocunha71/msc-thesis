    for i:= len(word) - 2; i >= 1; i-- {
        if !IsVowel(word[i]) && IsVowel(word[i+1]) && IsVowel(word[i-1]) {
            return string(word[i])
        }
    }
    return ""
}

func IsVowel(b byte) bool {
    return bytes.ContainsRune("aeiouAEIOU", rune(b))
}

func main() {
    fmt.Println(GetClosestVowel("yogurt")) // ==> "u"
    fmt.Println(GetClosestVowel("FULL"))   // ==> "U"
    fmt.Println(GetClosestVowel("quick"))  // ==> ""
    fmt.Println(GetClosestVowel("ab"))     // ==> ""
}

*/

import (
	"fmt"
	"strings"
)

func GetClosestVowel(word string) string {
	for i := len(word) - 1; i > 0; i-- {
		if !strings.ContainsRune("aeiouAEIOU", rune(word[i])) &&
			strings.ContainsRune("aeiouAEIOU", rune(word[i-1])) &&
			strings.ContainsRune("aeiouAEIOU", rune(word[i+1])) {
			return string(word[i])
		}
	}
	return ""
}

func main() {
	fmt.Print