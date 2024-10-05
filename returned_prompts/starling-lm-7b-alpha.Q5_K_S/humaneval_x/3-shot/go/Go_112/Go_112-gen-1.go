    s_ = strings.Replace(s,""+c,"",-1)
    result := " "
    if s_ == s_[len(s_)-1:len(s_):-1]{
        result = "True"
    }else {
        result = "False"
    }
    return [2]interface{}{s_ , result}
}



