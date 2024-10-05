    vector<int> third;
    for(int i=0;i<l.size();i++)
        if((i+1)%3 == 0)
            third.push_back(l[i]);
    sort(third.begin(), third.end());
    for(int i=0, j=0;i<l.size();i++)
        if((i+1)%3 == 0)
            l[i] = third[j++];
    return l;
}


