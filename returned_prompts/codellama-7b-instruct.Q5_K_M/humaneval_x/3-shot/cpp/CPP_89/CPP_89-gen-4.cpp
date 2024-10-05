    string result;
    char ch;
    for (int i=0;i<s.length();i++)
    {
        ch=s[i];
        if (ch>='a' && ch<='z')
        ch=(ch-'a'+(ch-'a'*2))+'a';
        if (ch>='A' && ch<='Z')
        ch=(ch-'A'+(ch-'A'*2))+'A';
        result+=ch;
    }
    return result;
}



