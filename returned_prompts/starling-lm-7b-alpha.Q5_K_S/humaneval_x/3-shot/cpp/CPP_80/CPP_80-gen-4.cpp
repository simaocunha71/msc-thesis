    if (s.length()<3) return false;
    if (s.length()==3) return true;
    if (s.length()==4)
    {
        if (s[0]==s[1]&&s[1]==s[2]) return false;
        else return true;
    }

    if (s[0]==s[1]||s[1]==s[2]) return false;
    if (s[0]==s[2]||s[2]==s[1]) return false;
    return true;
}



