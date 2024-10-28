    string s = to_string(x);
    int l = s.length();
    if (shift >= l)
    {
        shift = l-shift;
        for (int i=0;i<l/2;i++)
        {
            char tmp = s[i];
            s[i] = s[l-i-1];
            s[l-i-1] = tmp;
        }
        return s;
    }
    char tmp = s[l-shift-1];
    for (int i=l-shift;i<l-1;i++)
    {
        s[i] = s[i+1];
    }
    s[l-1] = tmp;
    return s;
}



