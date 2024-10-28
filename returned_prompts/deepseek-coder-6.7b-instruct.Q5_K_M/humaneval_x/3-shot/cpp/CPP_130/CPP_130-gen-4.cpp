    vector<int> tri;
    if (n==0) return tri;
    if (n==1) {tri.push_back(1); return tri;}
    if (n==2) {tri.push_back(1); tri.push_back(3); return tri;}
    tri.push_back(1); tri.push_back(3); tri.push_back(2);
    for (int i=3;i<=n;i++)
    {
        if (i%2==0)
        tri.push_back(1+i/2);
        else
        tri.push_back(tri[i-1]+tri[i-2]+tri[i+1]);
    }
    return tri;
}


