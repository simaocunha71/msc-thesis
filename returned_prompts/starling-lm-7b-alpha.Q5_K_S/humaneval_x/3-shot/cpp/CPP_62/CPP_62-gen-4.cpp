    int i;
    int len=xs.size();
    vector<float> res(len-1,0);
    for (i=0;i<len-1;i++)
    res[i]=xs[i+1];
    res[0]+=1;
    return res;
}

