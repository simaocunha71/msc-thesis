    int count=0;
    for (int i=0;i<s.length();i++)
    {
        char c=s[i];
        char c2=toupper(c);
        if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='y')
        count+=1;
    }
    return count;
}

