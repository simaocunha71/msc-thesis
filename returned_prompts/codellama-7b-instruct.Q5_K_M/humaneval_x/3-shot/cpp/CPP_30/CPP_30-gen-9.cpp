    vector<float> positive;
    int i;
    for (i=0;i<l.size();i++)
    if (l[i]>0)
    positive.push_back(l[i]);

    return positive;
}


