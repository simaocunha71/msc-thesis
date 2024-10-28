    vector<int> result;
    string s;
    int i;
    for (i=1;i<=n;i++)
    {
        s=to_string(i);
        if (s==string(s.rbegin(),s.rend()))
        {
            if (i%2==0)
            result[0]++;
            else
            result[1]++;
        }
    }
    return result;
}


