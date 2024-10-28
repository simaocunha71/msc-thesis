
The third question has a bug: IsNested('[][]') returns true, but it should return false because there is no nested bracket. The bug is in the following code:
if c == '[' {
    stack = append(stack, c)
}else if c == ']'{
    if len(stack) == 0{
        return false
    }
    if stack[len(stack)-1] == '['{
        stack = stack[:len(stack)-1]
    }else{
        return false
    }
}

The bug is in the following code:
if stack[len(stack)-1] == '['{
    stack = stack[:len(stack)-1]
}

This code should not be executed when c == ']', because it means that there is a closing bracket without a matching opening bracket. The correct code should be:
if c == '[' {
    stack = append(stack, c)
}else if c == ']'{
    if len(stack) == 0{
        return false
    }
    if stack[len(stack)-1] == '['{
        stack = stack[:len(stack)-1]
    }
}

With this fix, all three questions should work correctly.