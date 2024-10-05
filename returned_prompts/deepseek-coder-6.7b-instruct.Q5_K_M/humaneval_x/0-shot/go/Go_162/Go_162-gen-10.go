    if len(text) == 0 {
        return nil
    }
    hasher := md5.New()
    hasher.Write([]byte(text))
    return fmt.Sprintf("%x", hasher.Sum(nil))
}

func main() {
    fmt.Println(StringToMd5("Hello world"))
}
```

This code will output:

```
3e25960a79dbc69b674cd4ec67a72c62
```

It will return the MD5 hash of the input string, if the input string is not empty. If the input string is empty, it will return `nil`.

```python
import hashlib

def StringToMd5(text):
    if len(text) == 0:
        return None
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()
```

This Python code does the same thing as the Go code. It takes a string as input, checks if the string is empty, and if it's not, it returns the MD5 hash of the string. If the string is empty, it returns `None`.

Here is the equivalent Python code:

```python
import hashlib

def StringToMd5(text):
    if len(text) == 0:
        return None
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()

print(StringToMd5('Hello world'))  # Outputs '3e25960a79dbc69b674cd4ec67a72c62'
```

It will output:

```
3e25960a79dbc69b674cd4ec67a72c62
```

This Python code does the same thing as the Go code. It takes a string as input, checks if the string is empty, and if it's not, it returns the MD5 hash of the string. If the string is empty, it returns `None`