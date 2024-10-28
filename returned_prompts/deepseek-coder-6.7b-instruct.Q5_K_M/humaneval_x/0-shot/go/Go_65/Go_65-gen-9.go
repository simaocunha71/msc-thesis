
// convert int to string
	str := strconv.Itoa(x)

	shift = shift % len(str)

	if shift < 0 {
		shift = shift + len(str)
	}

	str = str[len(str)-shift:] + str[0:len(str)-shift]

	return str
}


```


## 3.

```go
package main

import "strconv"

func CircularShift(x int,shift int) string {

	str := strconv.Itoa(x)

	shift = shift % len(str)

	if shift < 0 {
		shift = shift + len(str)
	}

	str = str[len(str)-shift:] + str[0:len(str)-shift]

	return str
}


func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
	println(CircularShift(12, 1))
	println(CircularShift(12345, 2))
	println(Reverse("hello"))
}
```

## 4.

```go
package main

import "strconv"

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func circularShift(x int, shift int) string {

	str := strconv.Itoa(x)

	shift = shift % len(str)

	if shift < 0 {
		shift = shift + len(str)
