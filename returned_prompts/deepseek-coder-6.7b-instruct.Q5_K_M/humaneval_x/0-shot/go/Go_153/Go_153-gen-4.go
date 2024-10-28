    max_strength := math.MinInt64
    strongest_extension := ""

    for _, extension := range extensions {
        cap, sm := count_upper_lower(extension)
        strength := cap - sm
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}

func count_upper_lower(str string) (cap int, sm int) {
    for _, ch := range str {
        if 'A' <= ch && ch <= 'Z' {
            cap++
        } else if 'a' <= ch && ch <= 'z' {
            sm++
        }
    }
    return cap, sm
}

```

### Go
```go

import (
	"fmt"
	"strings"
	"unicode"
)

func countUpperLower(str string) (cap, sm int) {
	for _, ch := range str {
		if unicode.IsUpper(ch) {
			cap++
		} else if unicode.IsLower(ch) {
			sm++
		}
	}
	return cap, sm
}

func StrongestExtension(class_name string, extensions []string) string {
	maxStrength := int('Z'-'A') + 1
	strongestExtension := extensions[0]

	for _, extension := range extensions {
		cap, sm := countUpperLower(extension)
		strength := cap - sm
		if strength > maxStrength {
			maxStrength = strength
			strongestExtension = extension
		}
	}

	return fmt.Sprintf("%s.%s", class_name, strongestExtension)
}

```

### JavaScript
```javascript

function countUpperLower(str) {
    let cap = 0, sm = 0;
    for(let i = 0; i < str.length; i++) {
        if(str[i] === str[i].toUpperCase()) {
            cap++;
        } else if(str[i] === str[