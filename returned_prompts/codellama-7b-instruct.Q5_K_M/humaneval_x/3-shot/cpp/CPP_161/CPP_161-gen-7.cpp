    int i;
    int len = s.length();
    string res = "";
    bool is_letter = false;
    for (i=0;i<len;i++)
    {
        if (s[i]>='A' && s[i]<='Z')
        {
            res += tolower(s[i]);
            is_letter = true;
        }
        else if (s[i]>='a' && s[i]<='z')
        {
            res += toupper(s[i]);
            is_letter = true;
        }
        else
        {
            res += s[i];
        }
    }
    if (!is_letter)
    {
        for (i=0;i<len;i++)
        res[i] = toupper(res[i]);
    }
    return res;
}


