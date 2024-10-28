```go
import (
    "regexp"
)

func IsBored(S string) int {
    r := regexp.MustCompile(`(?i)(^|\.|\?|\!)\s*I\s`)
    return len(r.FindAllString(S, -1))
}
```
