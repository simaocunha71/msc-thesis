    int i;
    bool has_letter=false;
    for (i=0;i<s.length();i++)
    if (isalpha(s[i]))
    has_letter=true;
    if (!has_letter)
    return string(s.rbegin(), s.rend());
    string result;
    for (i=0;i<s.length();i++)
    if (isalpha(s[i]))
    result+=toupper(s[i]);
    else
    result+=s[i];
    return result;
}


