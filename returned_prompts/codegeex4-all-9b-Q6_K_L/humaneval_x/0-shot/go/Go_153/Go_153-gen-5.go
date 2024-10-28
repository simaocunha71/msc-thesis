```go
func StrongestExtension(class_name string, extensions []string) string {
    var strongExt = extensions[0]
    var strongExtScore = getScore(strongExt)

    for _, ext := range extensions {
        score := getScore(ext)
        if score < strongExtScore {
            strongExtScore = score
            strongExt = ext
        }
    }

    return class_name + "." + strongExt
}

func getScore(ext string) float64 {
    score := 0
    for _, c := range ext {
        if c >= 'A' && c <= 'Z' {
            score++
        } else if c >= 'a' && c <= 'z' {
            score--
        }
    }
    return float64(score)
}
```
