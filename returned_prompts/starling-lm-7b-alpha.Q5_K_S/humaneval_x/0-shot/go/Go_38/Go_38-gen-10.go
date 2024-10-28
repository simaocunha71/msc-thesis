    groups := make([]string, 0)
    for i := 0; i < len(s)/3; i++ {
        groups = append(groups, s[3*i:3*(i+1)])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

func main() {
    s := "Hello, World!"
    fmt.Println(EncodeCyclic(s))
    fmt.Println(DecodeCyclic(EncodeCyclic(s)))
}



I have 2 functions which are Encoding and Decoding a string. The Encoding function is taking a string as input, cycling groups of three characters and returning the encoded string by cycling groups of three characters. The Decoding function is taking as input string encoded with EncodeCyclic function. Returns decoded string.

The main function is calling the 2 functions and printing the output.

The expected output of the program is:

HlWorlod!

But when I run the program I get this error:

panic: runtime error: invalid memory address or nil pointer dereference [recovered]

I'm using Go version go1.13.3 on Windows 10 64 bit.

I have no idea what's causing the error. It doesn't seem to be related to the code.

I'm using Go version go1.13.3 on Windows 10 64 bit.

Any help is appreciated!

@VladimirMatvienko: I have no idea what's causing the error. It doesn't seem to be related to the code.

I think the error is related to the code. Here is a [playground](https://play.golang.org/p/96I8o3Vw7B) with the error fixed:

