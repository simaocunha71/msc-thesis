    int count=0;
    char c;
    for (int i=0;i<s.length();i++)
    {
        c=s[i];
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='y')
        count+=1;
    }
    return count;
}


