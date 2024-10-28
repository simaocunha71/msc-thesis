    int i;
    vector<float> ret;
    ret.resize(xs.size());
    for (i=0;i<xs.size();i++)
    {
        if (i==0)
        {
            ret[i]=xs[i];
        }
        else
        {
            ret[i]=ret[i-1]*i+xs[i];
        }
    }
    return ret;
}



