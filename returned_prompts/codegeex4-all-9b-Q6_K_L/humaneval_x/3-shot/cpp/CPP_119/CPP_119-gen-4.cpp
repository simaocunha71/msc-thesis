    int open=0,close=0;
    string s1=lst[0],s2=lst[1];
    int i,j;
    for (i=0;i<s1.length();i++)
    if (s1[i]=='(')
    open+=1;
    for (i=0;i<s2.length();i++)
    if (s2[i]=='(')
    open+=1;
    for (i=0;i<s1.length();i++)
    if (s1[i]==')')
    close+=1;
    for (i=0;i<s2.length();i++)
    if (s2[i]==')')
    close+=1;

    if (open==close)
    return "Yes";
    else
    return "No";
}

