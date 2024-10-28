    int i,orange_count=0,apple_count=0;
    char ch;
    for (i=0;i<s.length();i++)
    {
        ch=s[i];
        if (ch=='a')
        apple_count+=1;
        if (ch=='o')
        orange_count+=1;
    }
    return n-apple_count-orange_count;
}




