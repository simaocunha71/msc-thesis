for _, c := range date {
    switch c {
    case '-':
        continue A
    case '/':
        return false
    }
}

return true
}
