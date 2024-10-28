    int i;
    vector<float> positive_l;
    for (i=0;i<l.size();i++)
    if (l[i]>0)
    positive_l.push_back(l[i]);
    return positive_l;
}

