    int i;
    for  (i=0; i<str.length(); i++)
    {
        if  (islower(str[i]))
            str[i] = toupper(str[i]);
        else
            str[i] = tolower(str[i]);
    }
    return str;
}

