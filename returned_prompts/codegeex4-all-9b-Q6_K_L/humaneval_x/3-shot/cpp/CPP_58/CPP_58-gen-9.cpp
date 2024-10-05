    vector<int> common_elements;
    int i;
    for (i=0;i<l1.size();i++)
    if (find(common_elements.begin(),common_elements.end(),l1[i])==common_elements.end())
    common_elements.push_back(l1[i]);
    for (i=0;i<l2.size();i++)
    if (find(common_elements.begin(),common_elements.end(),l2[i])==common_elements.end())
    common_elements.push_back(l2[i]);
    sort(common_elements.begin(),common_elements.end());
    return common_elements;
}

