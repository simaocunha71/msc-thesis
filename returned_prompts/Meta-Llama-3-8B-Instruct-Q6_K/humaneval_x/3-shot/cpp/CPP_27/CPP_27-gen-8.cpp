    string result;
    for (int i=0;i<str.length();i++)
    {
        char c=str[i];
        if (c>='a' && c<='z')
        {
            c=c-'a'+'A';
        }
        else if (c>='A' && c<='Z')
        {
            c=c-'A'+'a';
        }
        result+=c;
    }
    return result;
}

