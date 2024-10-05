
// initialize a stack.
s := []rune{}

// iterate through the string.
for _, b := range brackets {

    // if the bracket is an opening bracket, push it onto the stack.
    if b == '<' {
        s = append(s, b)
    } else {

        // if the stack is empty, return false.
        if len(s) == 0 {
            return false
        }

        // pop the last bracket from the stack.
        s = s[:len(s)-1]
    }
}

// if the stack is empty, return true. otherwise, return false.
if len(s) == 0 {
    return true
}
return false
}


E:

// initialize a stack.
s := []rune{}

// iterate through the string.
for _, b := range brackets {

    // if the bracket is an opening bracket, push it onto the stack.
    if b == '<' {
        s = append(s, b)
    } else {

        // if the stack is empty, return false.
        if len(s) == 0 {
            return false
        }

        // pop the last bracket from the stack.
        s = s[:len(s)-1]
    }
}

// if the stack is empty, return true. otherwise,