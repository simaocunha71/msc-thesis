```go
import (
    "crypto/md5"
    "encoding/hex"
)

func StringToMd5(text string) string {
    if text == "" {
        return ""
    }
    hash := md5.Sum([]byte(text))
    return hex.EncodeToString(hash[:])
}
```