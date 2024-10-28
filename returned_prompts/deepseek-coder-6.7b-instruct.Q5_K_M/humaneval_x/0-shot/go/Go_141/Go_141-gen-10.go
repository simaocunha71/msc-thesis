    if file_name == ""{
        return "No"
    }

B:
    split_file_name := strings.Split(file_name, ".")
    if len(split_file_name) != 2 {
        return "No"
    }

C:
    if !(split_file_name[0][0] >= 'a' && split_file_name[0][0] <= 'z' || split_file_name[0][0] >= 'A' && split_file_name[0][0] <= 'Z') {
        return "No"
    }

D:
    count := 0
    for _, char := range split_file_name[0] {
        if char >= '0' && char <= '9' {
            count++
        }
    }
    if count > 3 {
        return "No"
    }

E:
    if split_file_name[1] != "txt" && split_file_name[1] != "exe" && split_file_name[1] != "dll" {
        return "No"
    }

    return "Yes"
}
```

##### [Solution](https://www.codewars.com/kata/581c06b04f49441724c5445fa/solutions/go)

```go
package kata

import (
	"strings"
	"unicode"
)

func FileNameCheck(file_name string) string {
	if len(file_name) == 0 {
		return "No"
	}
	parts := strings.Split(file_name, ".")
	if len(parts) != 2 || len(parts[0]) == 0 || len(parts[1]) != 3 {
		return "No"
	}
	if !unicode.IsLetter(rune(parts[0][0])) {
		return "No"
	}
	count := 0
	for _, chr := range parts[0] {
		if unicode.IsDigit(chr) {
			count++
		}
	}
	if