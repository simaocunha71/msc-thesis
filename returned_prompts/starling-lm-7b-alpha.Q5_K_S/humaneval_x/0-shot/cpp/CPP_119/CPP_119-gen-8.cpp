    for(int i=0;i<lst.size();i++)
    {
        if(lst[i]=="(")
        {
            lst[i]=")";
        }
    }
    string s,t;
    int i,j,count=0,c=0;
    for(i=0;i<lst.size();i++)
    {
        s=lst[i];
        if(s[0]=='(')
        {
            count++;
        }
        else
        {
            count--;
        }
    }
    if(count<0)
    {
        return "No";
    }
    for(i=0;i<lst.size();i++)
    {
        t=lst[i];
        if(t[0]==')')
        {
            c++;
        }
        else
        {
            c--;
        }
    }
    if(c!=count)
    {
        return "No";
    }
    return "Yes";
}






































































































































































































































































