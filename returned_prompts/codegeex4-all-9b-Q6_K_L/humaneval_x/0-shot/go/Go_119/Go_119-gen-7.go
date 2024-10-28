```go
func MatchParens(lst []string) string {
  open := 0
  close := 0
  for _, v := range lst {
    for _, w := range v {
      switch w {
      case '(':
        open++
      case ')':
        close++
      }
    }
  }
  if open == close {
    return "Yes"
  } else {
    return "No"
  }
}
```
