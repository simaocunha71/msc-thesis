    vector<int> tri_vector;
    if (n==0)
    {
        tri_vector.push_back(1);
        return tri_vector;
    }
    if (n==1)
    {
        tri_vector.push_back(1);
        tri_vector.push_back(3);
        return tri_vector;
    }
    tri_vector.push_back(1);
    tri_vector.push_back(3);
    int i=2;
    while (i<=n)
    {
        if (i%2==0)
        {
            tri_vector.push_back(1+(i/2));
        }
        else
        {
            tri_vector.push_back(tri_vector[i-1]+tri_vector[i-2]+tri_vector[i+1]);
        }
        i+=1;
    }
    return tri_vector;
}

