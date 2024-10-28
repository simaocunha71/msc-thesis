    int a,b,c,d;
    int i;
    a=0;
    b=0;
    c=0;
    d=0;
    for (i=0;i<x.length();i++)
    {
        if (x[i]=='/')
        {
            a=atoi(x.substr(0,i).c_str());
            b=atoi(x.substr(i+1).c_str());
            break;
        }
    }
    for (i=0;i<n.length();i++)
    {
        if (n[i]=='/')
        {
            c=atoi(n.substr(0,i).c_str());
            d=atoi(n.substr(i+1).c_str());
            break;
        }
    }
    return (a*d)%b==0 && (c*b)%d==0;
}


