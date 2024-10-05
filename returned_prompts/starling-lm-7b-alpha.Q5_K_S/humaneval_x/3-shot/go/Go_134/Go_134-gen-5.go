    if len(txt)==0{
        return false
    }
    if txt[len(txt)-1]>='a' && txt[len(txt)-1]<='z' || txt[len(txt)-1]>='A' && txt[len(txt)-1]<='Z':
        return strings.Index(txt, " ")+len(txt)-1!=len(txt)-1
    return false
}



