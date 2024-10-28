    string result;
    for (int i=0;i<s.length();i++)
    {
        if (isalpha(s[i]))
        {
            char c=s[i];
            if (islower(c))
                c=tolower(c);
            else
                c=toupper(c);
            result+=c;
        }
        else
            result+=s[i];
    }
    reverse(result.begin(), result.end());
    return result;
}