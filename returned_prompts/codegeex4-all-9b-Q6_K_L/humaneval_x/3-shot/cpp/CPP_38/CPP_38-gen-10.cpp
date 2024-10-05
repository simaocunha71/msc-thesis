    string x, output;
    int i;
    int l=s.length();
    int num=(l+2)/3;
    for (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if (x.length()==3) x=x[x.length()-1]+x.substr(0,x.length()-1);
        output=output+x;
    }
    return output;
}

