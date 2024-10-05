    for(int i=0;i<s0.size();i++)
    {
        for(int j=0;j<s1.size();j++)
        {
            if(s0[i]==s1[j])
            {
                goto A;
            }
        }
        return false;
    }
    return true;
}
int main()
{
    string a,b;
    while(cin>>a>>b)
    {
        if(same_chars(a,b))
        {
            printf("true\n");
        }
        else
        {
            printf("false\n");
        }
    }
    return 0;
}
