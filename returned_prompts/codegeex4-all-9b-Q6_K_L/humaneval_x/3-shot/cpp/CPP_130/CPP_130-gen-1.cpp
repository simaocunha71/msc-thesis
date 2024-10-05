    vector<int> tri_seq;
    int i;
    tri_seq.push_back(1);
    tri_seq.push_back(3);
    for (i=2;i<n;i++)
    {
        if (i%2==0)
        tri_seq.push_back(1+i/2);
        if (i%2==1)
        tri_seq.push_back(tri_seq[i-1]+tri_seq[i-2]+tri_seq[i+1]);
    }
    return tri_seq;
}

