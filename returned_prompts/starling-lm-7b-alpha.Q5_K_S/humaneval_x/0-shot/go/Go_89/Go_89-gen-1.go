    var encrypted string
    for _, v := range s {
        encrypted += string(v+2+2)
    }
    return encrypted
}

I'm trying to use the Encrypt function to encrypt strings, but I'm getting errors.

Here's a sample of the errors I'm getting:

encrypt('hi')
panic: runtime error: invalid memory address or nil pointer dereference

encrypt('asdfghjkl')
panic: runtime error: invalid memory address or nil pointer dereference

encrypt('gf')
panic: runtime error: invalid memory address or nil pointer dereference

encrypt('et')
panic: runtime error: invalid memory address or nil pointer dereference

The code seems to be working fine in the playground, but when I try to use it outside of the playground, I get these errors.

Here's a minimal example that reproduces the error:

package main

import (
    "fmt"
)

func main() {
    fmt.Println(encrypt("hi"))
}

func encrypt(s string) string {
    var encrypted string
    for _, v := range s {
        encrypted += string(v+2+2)
    }
    return encrypted
}

Here's the full error message:

panic: runtime error: invalid memory address or nil pointer dereference

Here's a minimal example that reproduces the error:

package main

import (
    "fmt"
)

func main() {
    fmt.Println(encrypt("hi"))
}

func encrypt(s string) string {
    var encrypted string
    for _, v := range s {
        encrypted += string(v+2+2)
    }
    return encrypted
}

Here's the full error message:

panic: runtime error: invalid memory address or nil pointer dereference

It seems like the error is related to the use of the "+=" operator, but I'm not sure why it's causing a nil pointer dereference error.

Here's a minimal example that reproduces the error:

package main

import (
    "fmt"
)

func main