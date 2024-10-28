    int l=s.length();
    string output,x;
    int i;
    for (i=0;i<l;i++)
    {
        x=s[i]+s[i+1];
        output=output+x[1];
    }
    return output;
}


