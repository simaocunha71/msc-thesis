    vector<float> all_parens;
    float chr;
    int i;
    for (i=0;i<xs.size();i++)
    {
        chr=xs[i]*i;
        all_parens.push_back(chr);
    }
    return all_parens;
}

