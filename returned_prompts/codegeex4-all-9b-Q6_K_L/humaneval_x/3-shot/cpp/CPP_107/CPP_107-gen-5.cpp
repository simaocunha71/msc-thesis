    int i,j;
    string s;
    int even=0,odd=0;
    for (i=1;i<=n;i++)
    {
        s=to_string(i);
        if (s==string(s.rbegin(),s.rend())){
            if (i%2==0)
            even+=1;
            else
            odd+=1;
        }
    }
    vector<int> vec={even,odd};
    return vec;
}

