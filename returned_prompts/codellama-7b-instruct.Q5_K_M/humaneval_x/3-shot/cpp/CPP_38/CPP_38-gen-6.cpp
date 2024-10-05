    string x;
    int l=s.length();
    string output;
    int i;
    for (i=0;i<l;i++)
    {
        x=s[i];
        if (i>0 && i%3==0) x=s[i-1]+x;
        output+=x;
    }
    return output;
}



