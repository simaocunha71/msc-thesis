    vector<int> res(2);
    int i;
    for (i=1;i<=n;i++)
    {
        string s=to_string(i);
        if (s==string(s.rbegin(),s.rend()))
        {
            if (i%2==0) res[0]+=1;
            else res[1]+=1;
        }
    }
    return res;
}



