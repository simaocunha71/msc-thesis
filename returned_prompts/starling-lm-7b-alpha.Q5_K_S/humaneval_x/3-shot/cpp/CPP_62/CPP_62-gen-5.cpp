    int i,n;
    vector<float> result;
    n=xs.size();
    result.resize(n);

    for (i=1;i<n;i++)
    {
        result[i-1]=xs[i]*i;
    }

    return result;
}



