    string base10="";
    string base="";
    int i=0;
    while (x>0)
    {
        base10=base10+char(x%10+48);
        x=x/10;
        i+=1;
    }
    int n=base10.length();
    for (int i=n-1;i>=0;i-=1)
    base=base+base10[i];
    return base;
}

