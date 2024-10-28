    int i;
    int even=0,odd=0;
    for (i=1;i<=n;i++)
    {
        string s=to_string(i);
        string r=s;
        reverse(s.begin(),s.end());
        if (s==r)
        {
            if (i%2==0)
                even++;
            else
                odd++;
        }
    }
    vector<int> output;
    output.push_back(even);
    output.push_back(odd);
    return output;
}

