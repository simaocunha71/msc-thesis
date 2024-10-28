    vector<int> res;
    int tri_n;
    int i;
    res.push_back(3);
    if (n<2)
    return res;
    tri_n=3;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        {
            tri_n=tri_n/2+1;
        }
        else
        {
            tri_n=res[res.size()-1]+res[res.size()-2]+res[res.size()-3];
        }
        res.push_back(tri_n);
    }
    return res;
}



