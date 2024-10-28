    vector<float> pos;
    float tmp;
    int i;
    for (i=0;i<l.size();i++)
    {
        tmp=l[i];
        if (tmp>=0)
        pos.push_back(tmp);
    }
    return pos;
}


