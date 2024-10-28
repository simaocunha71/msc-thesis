    vector<int> thirds;
    for  (int i=2;i<l.size();i+=3)
    thirds.push_back(l[i]);

    sort(thirds.begin(),thirds.end());

    for  (int i=2, j=0;i<l.size();i+=3,++j)
    l[i]=thirds[j];

    return l;
}


