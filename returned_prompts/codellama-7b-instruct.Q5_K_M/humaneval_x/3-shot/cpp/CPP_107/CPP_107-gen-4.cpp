    vector<int> result(2,0);
    int i;
    for (i=1;i<=n;i++){
        string s=to_string(i);
        if (s==string(s.rbegin(),s.rend()))
        if (i%2==0)
        result[0]+=1;
        else
        result[1]+=1;
    }
    return result;
}


