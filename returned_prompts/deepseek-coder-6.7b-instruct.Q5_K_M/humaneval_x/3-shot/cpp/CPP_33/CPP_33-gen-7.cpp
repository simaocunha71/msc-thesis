    vector<int> third;
    for  (int i=2; i<l.size(); i+=3)
        third.push_back(l[i]);
    sort(third.begin(), third.end());
    for  (int i=2, j=0; i<l.size(); i+=3, ++j)
        l[i] = third[j];
    return l;
}


