    int i=0;
    string s="";
    for (i=0;i<lst.size();i++)
    s+=lst[i];
    int level=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='(')
        level+=1;
        if (s[i]==')')
        level-=1;
        if (level<0)
        return "No";
    }
    if (level==0)
    return "Yes";
    return "No";
}




