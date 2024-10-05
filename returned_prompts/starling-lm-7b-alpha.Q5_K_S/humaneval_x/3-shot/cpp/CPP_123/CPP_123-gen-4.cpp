    vector<int> all_odd;
    vector<int> collatz_seq;
    int i,j;
    int next_num;
    if (n==1)
    {
        vector<int> one={1};
        all_odd.push_back(1);
        return all_odd;
    }
    collatz_seq.push_back(n);
    for (i=0;i<collatz_seq.size();i++)
    {
        next_num=collatz_seq[i];
        if (next_num%2==1)
        {
            all_odd.push_back(next_num);
        }
        if (next_num%2==0)
        {
            next_num/=2;
            collatz_seq.push_back(next_num);
        }
    }
    sort(all_odd.begin(), all_odd.end());
    return all_odd;
}


