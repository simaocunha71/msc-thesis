    int i;
    string result="";
    for (i=0;i<s.length();i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            result+=toupper(s[i]);
            else
            result+=tolower(s[i]);
        }
        else
        result+=s[i];
    }
    return result;
}


