    int i;
    int count=0;
    for (i=0;i<s.length();i++)
    if (s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
    if (i%2==0)
    count+=1;
    return count;
}


