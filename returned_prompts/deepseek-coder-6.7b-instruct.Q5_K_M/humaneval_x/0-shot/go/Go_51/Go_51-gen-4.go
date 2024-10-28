    var re = regexp.MustCompile(`(?i)[aeiou]`)
    return re.ReplaceAllString(text, "")
}


A: Here's how you can do it using the Go standard library:

```go
import (
    "strings"
)

func RemoveVowels(text string) string {
    const vowels = "aeiouAEIOU"

    return strings.Map(func(r rune) rune {
        if strings.ContainsRune(vowels, r) {
            return -1
        }
        return r
    }, text)
}
```

This function uses the `strings.Map` function, which transforms each rune in the input string using the provided function. If the rune is a vowel (as determined by the `strings.ContainsRune` function), the rune is replaced with `-1`, which `strings.Map` converts to `'\x00'`, effectively removing it from the output string.

Here's how you can use it:

```go
func main() {
    fmt.Println(RemoveVowels("Hello, world!"))  // Outputs: "Hll, wrld!"
}
```

This code will remove all the vowels from the string "Hello, world!" and print "Hll, wrld!".

Note: This code only removes ASCII vowels. If you need to remove Unicode vowels (like ä, , , æ, , å), you will need to adjust the `vowels` constant accordingly.

Also, be aware that this code treats uppercase and lowercase vowels as the same. If you want to treat them as separate, you can remove the `AEIOU` part from the `vowels` constant.

```go
const vowels = "aeiou"
```

This would make the function remove both uppercase and lowercase vowels.

```go
fmt.Println(RemoveVowels("Hello, world!"))  // Outputs: "Hll, wrld!"
```

This code will still remove all the vowels from the string "Hello, world!" and print