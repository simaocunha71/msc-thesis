    int i;
    for (i=0;i<str.length();i++)
    {
        if (islower(str[i]))
            str[i]=toupper(str[i]);
        if (isupper(str[i]))
            str[i]=tolower(str[i]);
    }
    return str;
}

