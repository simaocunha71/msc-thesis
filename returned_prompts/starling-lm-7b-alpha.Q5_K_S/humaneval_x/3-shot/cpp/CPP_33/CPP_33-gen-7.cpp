    vector<int> third;
    for (int i=0;i<l.size();i++)
    if (i%3==0)
    third.push_back(l[i]);
    sort(third.begin(),third.end());
    return third;
}



