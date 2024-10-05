    int len_a=a.size();
    int len_b=b.size();
    vector<int> result;
    int i,j;
    bool flag;
    for (i=0;i<len_a;i++)
    {
        flag=false;
        for (j=0;j<len_b;j++)
        {
            if (a[i]==b[j])
            {
                flag=true;
                break;
            }
        }
        if (flag==true)
        result.push_back(a[i]);
    }
    return result;
}

