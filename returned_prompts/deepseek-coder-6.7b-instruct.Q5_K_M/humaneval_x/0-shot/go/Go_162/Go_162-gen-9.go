    if text == "" {
        return nil
    }
    hasher := md5.New()
    hasher.Write([]byte(text))
    return fmt.Sprintf("%x", hasher.Sum(nil))
}


A: 
import (
    "crypto/md5"
    "fmt"
)

func StringToMd5(text string) *string {
    if text == "" {
        return nil
    }
    data := []byte(text)
    hash := md5.Sum(data)
    md5String := fmt.Sprintf("%x", hash)
    return &md5String
}

