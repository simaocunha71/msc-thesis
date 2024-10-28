    if(a.length()<b.length())return false;
    for(int i=0;i<a.length();i++)
    {
        bool flag=true;
        for(int j=0;j<b.length();j++)
        {
            if(i+j>=a.length())flag=false;
            if(b[j]!=a[i+j])flag=false;
        }
        if(flag)return true;
    }
    for(int i=0;i<b.length();i++)
    {
        bool flag=true;
        for(int j=0;j<b.length();j++)
        {
            if(i+j>=a.length())flag=false;
            if(b[j]!=a[i+j])flag=false;
        }
        if(flag)return true;
    }
    return false;
}
int main()
{
    string a,b;
    while(cin>>a>>b)
    {
        if(cycpattern_check(a,b))printf("true\n");
        else printf("false\n");
    }
    return 0;
}

*/


































































































































































































































