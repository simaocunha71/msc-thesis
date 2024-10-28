    vector<int> tri;
    int i;
    for(i=0;i<n+1;i++)
    {
        if(i==1)
        {
            tri.push_back(3);
        }
        else if(i%2==0)
        {
            tri.push_back(2);
        }
        else if(i%2==1)
        {
            tri.push_back(tri[i-1]+tri[i-2]+tri[i+1]);
        }
    }
    return tri;
}

