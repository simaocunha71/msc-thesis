    map<char,int> m;
    for(int i=0;i<test.length();i++)
    {
        char c=test[i];
        m[c]++;
    }
    return m;
}
int main()
{
    string test;
    cin>>test;
    map<char,int> m=histogram(test);
    map<char,int>::iterator it;
    int max=0;
    char c=' ';
    for(it=m.begin();it!=m.end();it++)
    {
        if(it->second>max)
        {
            max=it->second;
            c=it->first;
        }
    }
    if(max==1)
    {
        printf("{");
        for(it=m.begin();it!=m.end();it++)
        {
            if(it->first!=c)
            {
                printf("{");
                printf("%c",it->first);
                printf(",");
                printf("%d",it->second);
                printf("},");
            }
        }
        printf("}");
    }
    else
    {
        printf("{");
        for(it=m.begin();it!=m.end();it++)
        {
            if(it->second==max)
            {
                printf("{");
                printf("%c",it->first);
                printf(",");
                printf("%d",it->second);
                printf("},");
            }
        }
        printf("}");
    }
    return 0;
}

*/























































































































