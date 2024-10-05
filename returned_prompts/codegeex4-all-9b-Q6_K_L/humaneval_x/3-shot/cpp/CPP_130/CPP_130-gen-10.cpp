    vector<int> tri_num;
    if (n==0)
    return tri_num;
    tri_num.push_back(1);
    tri_num.push_back(3);
    int i;
    for (i=2;i<=n;i++)
    {
        if (i%2==0)
            tri_num.push_back(1+i/2);
        else
            tri_num.push_back(tri_num[i-1]+tri_num[i-2]+tri_num[i-3]);
    }
    return tri_num;
}