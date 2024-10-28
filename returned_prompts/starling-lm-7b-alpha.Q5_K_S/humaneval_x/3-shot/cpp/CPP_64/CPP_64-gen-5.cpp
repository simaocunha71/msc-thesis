    int count=0;
    char ch;
    for (int i=0;i<s.length();i++)
    {
        ch=s[i];
        if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' || ch=='y')
        count+=1;
    }
    return count;
}


