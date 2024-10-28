    vector<int> tri_seq;
    tri_seq.push_back(3);
    if (n>0)
    {
        tri_seq.push_back(1);
        if (n>1)
        tri_seq.push_back(1);
    }
    for (int i=3;i<=n;i++)
    {
        int sum=0;
        if (i%2==0)
        sum=1+(i/2);
        else
        {
            sum=tri_seq[i-1]+tri_seq[i-2];
        }
        tri_seq.push_back(sum);
    }
    return tri_seq;
}