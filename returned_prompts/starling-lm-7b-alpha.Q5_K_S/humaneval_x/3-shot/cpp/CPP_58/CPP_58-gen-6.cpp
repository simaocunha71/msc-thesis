    vector<int> unique_common_elems;
    vector<int> l3;
    int i,j;
    for (i=0;i<l1.size();i++)
    for (j=0;j<l2.size();j++)
    if (l1[i]==l2[j])
    {
        if (unique_common_elems.size()==0||unique_common_elems[unique_common_elems.size()-1]!=l1[i])
        unique_common_elems.push_back(l1[i]);
    }

    sort(unique_common_elems.begin(), unique_common_elems.end());
    return unique_common_elems;
}




