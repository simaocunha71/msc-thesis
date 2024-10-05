    if(txt.length()==0 || (txt[txt.length()-1]<'a' || txt[txt.length()-1]>'z') && (txt[txt.length()-1]<'A' || txt[txt.length()-1]>'Z'))
        return false;

    for(int i=0; i<txt.length()-1; i++)
        if(txt[i] == ' ' && txt[i+1] == txt[txt.length()-1])
            return false;

    return true;
}

