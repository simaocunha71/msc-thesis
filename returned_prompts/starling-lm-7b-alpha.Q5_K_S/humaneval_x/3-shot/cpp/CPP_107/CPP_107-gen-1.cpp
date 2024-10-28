    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    {
        string temp=to_string(i);
        int len=temp.length();
        if (len==1)
            continue;
        if (i%2==0)
            result[0]+=1;
        else
            result[1]+=1;
    }
    return result;
}



