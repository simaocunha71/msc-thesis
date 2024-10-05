    vector<int> sorted;
    for  (int i=0;i<l.size();i++)
        if  ((i+1)%3==0) sorted.push_back(l[i]);
    sort(sorted.begin(), sorted.end());
    for  (int i=0, j=0;i<l.size();i++)
        if  ((i+1)%3==0) l[i]=sorted[j++];
    return l;
}


