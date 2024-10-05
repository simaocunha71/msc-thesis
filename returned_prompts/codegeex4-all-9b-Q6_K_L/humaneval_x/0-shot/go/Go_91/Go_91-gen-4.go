```go
package kata

import (
    "regexp"
)

func IsBored(S string) int {
    re := regexp.MustCompile(`I\w*[.?!]`)
    return len(re.FindAllString(S, -1))
}
```
