    int count=0;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]=='a'||s[i]=='A'||s[i]=='e'||s[i]=='E'||s[i]=='i'||s[i]=='I'||s[i]=='o'||s[i]=='O'||s[i]=='u'||s[i]=='U'||s[i]=='y'||s[i]=='Y')
        count++;
    }
    return count;
}


