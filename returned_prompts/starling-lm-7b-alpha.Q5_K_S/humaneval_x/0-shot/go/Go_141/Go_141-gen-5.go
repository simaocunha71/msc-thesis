    var r = 0
    var c = 0
    for _, v := range file_name {
        if r == 0 && v >= 'a' && v <= 'z' {
            r = v
            c++
        } else if r != 0 && v >= 'a' && v <= 'z' {
            return "No"
        } else if v >= '0' && v <= '9' {
            c++
            if c > 3 {
                return "No"
            }
        } else if v == '.' {
            if c > 1 {
                return "No"
            }
        } else {
            return "No"
        }
    }

    if c != 2 {
        return "No"
    }

    var t string = file_name[r:]
    t = strings.ToLower(t)
    if t == "txt" || t == "dll" || t == "exe" {
        return "Yes"
    } else {
        return "No"
    }
}


































































































































































































































































