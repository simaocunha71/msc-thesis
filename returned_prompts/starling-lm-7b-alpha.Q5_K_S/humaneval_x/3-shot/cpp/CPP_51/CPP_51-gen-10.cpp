    string result="";
    char chr;
    int i;
    for (i=0;i<text.length();i++)
    {
        chr=tolower(text[i]);
        if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u')
        result+=chr;
    }
    return result;
}


