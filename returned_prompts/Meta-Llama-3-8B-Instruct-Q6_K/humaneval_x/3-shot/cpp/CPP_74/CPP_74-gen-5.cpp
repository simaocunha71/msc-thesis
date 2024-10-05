    vector<string> result;
    string s1,s2;
    int sum1=0,sum2=0;
    for (int i=0;i<lst1.size();i++)
    {
        s1=lst1[i];
        sum1+=s1.length();
    }
    for (int i=0;i<lst2.size();i++)
    {
        s2=lst2[i];
        sum2+=s2.length();
    }
    if (sum1<sum2)
    {
        result=lst1;
    }
    else if (sum1>sum2)
    {
        result=lst2;
    }
    else
    {
        result=lst1;
    }
    return result;
}