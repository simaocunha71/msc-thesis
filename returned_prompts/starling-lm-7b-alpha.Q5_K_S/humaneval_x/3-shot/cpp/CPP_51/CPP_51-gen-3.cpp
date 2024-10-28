    string result;
    char chr;
    for (int i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u' && chr!='A' && chr!='E' && chr!='I' && chr!='O' && chr!='U')
        result+=chr;
    }
    return result;
}



