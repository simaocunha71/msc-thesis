    words := strings.FieldsFunc(txt, func(r rune) bool {
        return r == ' ' || r == ','
    })
    if len(words) > 1 {
        return words
    }

    count := 0
    for _, r := range txt {
        if 'a' <= r && r <= 'z' {
            count++
        }
    }

    if count%2 != 0 {
        return count
    }

    return 0
}

func main() {
    fmt.Println(SplitWords("Hello world!"))  // ➞ ["Hello", "world!"]
    fmt.Println(SplitWords("Hello,world!"))  // ➞ ["Hello", "world!"]
    fmt.Println(SplitWords("abcdef"))  // ➞ 3
}
```

In the given code, we start by defining the function `SplitWords`. This function takes a string `txt` as input. We then check if `txt` contains whitespace or commas. If it does, we split `txt` at these characters and return the resulting words. If `txt` does not contain either of these characters, we count the number of lower-case letters in `txt` and return this count if it is odd. If the count is not odd, we return 0.

This function works by using the `strings.FieldsFunc` function to split `txt` at whitespace and commas. The `strings.FieldsFunc` function splits the string `txt` at each rune for which the function returns true. In this case, the function returns true if the rune is a whitespace or a comma.

The rest of the code is just a demonstration of how to use the `SplitWords` function. We call `SplitWords` with three different strings and print the results.

Note: The `SplitWords` function returns an interface{}, which means it can return any type. In this case, it returns a list of words (a slice of strings) if the input string contains whitespace or commas, and it returns an integer if the input string contains no whitespace or commas.

Also note that the `main` function is just a demonstration of how