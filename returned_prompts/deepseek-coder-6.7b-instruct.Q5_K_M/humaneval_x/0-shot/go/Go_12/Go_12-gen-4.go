if len(strings) == 0 {
  return nil
}

longest := strings[0]
for _, str := range strings {
  if len(str) > len(longest) {
    longest = str
  }
}

return longest
}
```

## Task 3

Write a Go function that takes a string as an argument and returns another string with the words in reversed order.

Example:

```
// Given "Hello World" it should return "World Hello"
```

```go
