    if len(txt) == 0 {
        return false
    }

B:
    if strings.HasSuffix(txt, " ") {
        return false
    }

C:
    if !strings.Contains(txt, " ") {
        return true
    }

D:
    if strings.HasSuffix(txt, " ") {
       