    vector<float> positive_numbers;
    int i;
    for (i=0;i<l.size();i++)
    if (l[i]>0)
    positive_numbers.push_back(l[i]);
    return positive_numbers;
}

