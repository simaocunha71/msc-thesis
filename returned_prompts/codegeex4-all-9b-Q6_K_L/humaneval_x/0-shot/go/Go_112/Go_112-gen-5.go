```go
func ReverseDelete(s,c string) [2]interface{} {
    var ret []rune
    for _, x := range s {
        if !strings.ContainsRune(c, x) {
            ret = append(ret, x)
        }
    }
    if len(ret) < 2 {
        return [2]interface{}{string(ret), false}
    }
    for i, j := 0, len(ret)-1; i < j; i, j = i+1, j-1 {
        if ret[i] != ret[j] {
            return [2]interface{}{string(ret), false}
        }
    }
    return [2]interface{}{string(ret), true}
}
```