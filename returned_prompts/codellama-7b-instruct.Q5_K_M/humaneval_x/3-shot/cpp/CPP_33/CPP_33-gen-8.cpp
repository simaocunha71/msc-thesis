    vector<int> l_new;
    int i;
    for (i=0;i<l.size();i++)
    if (i%3!=0)
    l_new.push_back(l[i]);
    else
    {
        sort(l.begin()+i, l.begin()+i+3);
        l_new.push_back(l[i]);
        l_new.push_back(l[i+1]);
        l_new.push_back(l[i+2]);
    }
    return l_new;
}



