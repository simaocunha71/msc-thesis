    if(txt.empty())
    return false;

    char last_char = txt[txt.length()-1];
    if(isalpha(last_char))
    {
        if(txt.length()==1)
        return true;
        else if(txt[txt.length()-2]==' ')
        return true;
    }
    return false;
}


