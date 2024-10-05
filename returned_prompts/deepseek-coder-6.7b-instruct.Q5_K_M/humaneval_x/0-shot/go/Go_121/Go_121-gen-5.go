
sum:=0

for i:=0; i<len(lst); i+=2 {
  if lst[i] % 2 != 0 {
    sum += lst[i]
  }
}

return sum
}

*/
package kata

func Solution(lst []int) int {
	sum := 0

	for i := 0; i < len(lst); i += 2 {
		if lst[i]%2 != 0 {
			sum += lst[i]
		}
	}

	return sum
}
/*

Code as below:

package kata

import (
  "strings"
  "unicode"
)

func ToWeirdCase(s string) string {
  str := ""
  for i, j := 0, 0; i < len(s); i++ {
    if unicode.IsLetter(rune(s[i])) {
      if j%2 == 0 {
        str += strings.ToUpper(string(s[i]))
      } else {
        str += strings.ToLower(string(s[i]))
      }
      j++
    } else {
      str += string(s[i])
      j = 0
    }
  }
  return str
}

*/

package kata

import (
	"strings"
	"unicode"
)

func ToWeirdCase(s string) string {
	str := ""
	for i, j := 0, 0; i < len(s); i++ {
		if unicode.IsLetter(rune(s[i])) {
			if j%2 == 0 {
				str += strings.ToUpper(string(s[i]))
			} else {
				str += strings.ToLower(string(s[i]))
			}
			j++
		} else {
			str += string(s[i])
			j = 0
		}
	}
	return str
}

// The function ToWeirdCase takes a string as argument and returns the same string but with every even indexed character in each word