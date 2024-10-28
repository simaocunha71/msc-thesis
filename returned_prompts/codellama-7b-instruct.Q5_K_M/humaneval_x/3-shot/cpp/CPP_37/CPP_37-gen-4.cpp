    vector<float> l_copy;
    for (int i=0;i<l.size();i++)
    l_copy.push_back(l[i]);

    sort(l_copy.begin()+1, l_copy.end()-1);
    return l_copy;
}



