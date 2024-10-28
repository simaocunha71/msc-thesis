    int n=a.size();
    int m=b.size();
    if(n!=m)
    {
        return "Incorrect Input";
    }
    string c="";
    while(n--)
    {
        if(a[n]=='0' && b[n]=='0')
        {
            c.push_back('0');
        }
        else if(a[n]=='0' && b[n]=='1')
        {
            c.push_back('1');
        }
        else if(a[n]=='1' && b[n]=='0')
        {
            c.push_back('1');
        }
        else
        {
            c.push_back('0');
        }
    }
    return c;
}




















