    vector<float> even_idx_elements;
    for(int i=0;i<l.size();i++)
        if(i%2==0)
            even_idx_elements.push_back(l[i]);
    sort(even_idx_elements.begin(), even_idx_elements.end());
    for(int i=0, j=0;i<l.size();i++)
        if(i%2==0)
            l[i]=even_idx_elements[j++];
    return l;
}

