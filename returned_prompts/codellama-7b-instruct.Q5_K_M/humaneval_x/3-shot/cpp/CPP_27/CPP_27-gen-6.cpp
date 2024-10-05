    string upper;
    string lower;
    char ch;
    int i;
    for (i=0;i<str.length();i++)
    {
        ch=str[i];
        if (ch>='a'&&ch<='z')
        upper+=ch-32;
        if (ch>='A'&&ch<='Z')
        lower+=ch+32;
    }
    return upper+lower;
}




