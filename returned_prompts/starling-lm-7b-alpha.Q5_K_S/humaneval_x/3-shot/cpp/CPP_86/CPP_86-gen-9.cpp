    string res="";
    char chr;
    char prev_chr=' ';
    for (chr=s[0];chr!='\0';chr=s[++i])
    {
        if (chr==' ')
        {
        res+=chr;
        prev_chr=' ';
        }
        else
        {
        sort(prev_chr+chr);
        res+=prev_chr+chr;
        prev_chr=' ';
        }
    }
    return res;
}


