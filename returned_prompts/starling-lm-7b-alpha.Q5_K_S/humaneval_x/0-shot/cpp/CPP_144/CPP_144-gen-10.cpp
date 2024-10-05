    int n1=0,d1=0,n2=0,d2=0;
    for(int i=0;i<x.length();i++)
    {
        if(x[i]=='/')
        {
            n1=atoi(x.substr(0,i).c_str());
            d1=atoi(x.substr(i+1,x.length()-i-1).c_str());
            break;
        }
    }
    for(int i=0;i<n.length();i++)
    {
        if(n[i]=='/')
        {
            n2=atoi(n.substr(0,i).c_str());
            d2=atoi(n.substr(i+1,n.length()-i-1).c_str());
            break;
        }
    }
    if((n2*d1)%d2==0)
    {
        printf("true\n");
        return true;
    }
    else
    {
        printf("false\n");
        return false;
    }
}


















































































































































































































































