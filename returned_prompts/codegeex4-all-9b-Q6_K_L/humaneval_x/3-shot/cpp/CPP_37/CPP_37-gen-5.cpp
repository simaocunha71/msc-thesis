    vector<float> even_l;
    for (int i=0;i<l.size();i+=2)
    even_l.push_back(l[i]);

    sort(even_l.begin(),even_l.end());

    int even_index=0;
    for (int i=0;i<l.size();i+=2)
    {
    l[i]=even_l[even_index];
    even_index+=1;
    }
    return l;
}

