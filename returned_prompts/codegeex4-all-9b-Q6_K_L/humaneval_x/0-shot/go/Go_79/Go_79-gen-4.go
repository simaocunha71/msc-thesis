```go
func DecimalToBinary(decimal int) string {
    var result string
    for decimal > 0 {
        result = strconv.Itoa(decimal % 2) + result
        decimal = decimal / 2
    }
    return "db" + result + "db"
}
```