The return type of your function is interface{}, and the fmt.Sprintf() function returns an *string (a pointer to a string). Since interface{} is a reference type, fmt.Sprintf() will return &(*string).

To fix the issue, you can change the return type of your function to *string:

```go
func StringToMd5(text string) *string {
    var h = md5.New()
    h.Write([]byte(text))
    return fmt.Sprintf("%x", h.Sum(nil))
}
```

Now, when you call StringToMd5("Hello world"), you will get a pointer to the md5 hash string:

```go
hash := StringToMd5("Hello world")
fmt.Println(*hash) // Prints: 3e25960a79dbc69b674cd4ec67a72c62
```

Note that the StringToMd5() function now returns a non-nil value even if the text string is empty:

```go
hash := StringToMd5("")
fmt.Println(*hash) // Prints:
```

This is because an empty string is still a valid string, and the md5.New().Sum(nil) will not return nil.

If you want to return nil when the input string is empty, you can add a check for it:

```go
func StringToMd5(text string) *string {
    if text == "" {
        return nil
    }
    var h = md5.New()
    h.Write([]byte(text))
    return fmt.Sprintf("%x", h.Sum(nil))
}
```

Now, when you call StringToMd5(""),