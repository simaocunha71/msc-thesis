    int a,b,c,d;
    int i,j;
    for (i=0;i<x.length();i++)
    if (x[i]=='/')
    {
        a=atoi(x.substr(0,i).c_str());
        b=atoi(x.substr(i+1,x.length()-i-1).c_str());
        break;
    }
    for (i=0;i<n.length();i++)
    if (n[i]=='/')
    {
        c=atoi(n.substr(0,i).c_str());
        d=atoi(n.substr(i+1,n.length()-i-1).c_str());
        break;
    }
    return (a*d)%b==0;
}


