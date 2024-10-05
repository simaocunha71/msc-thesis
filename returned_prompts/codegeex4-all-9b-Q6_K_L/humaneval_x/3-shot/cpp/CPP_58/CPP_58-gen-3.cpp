    vector<int> common_elements;
    int i,j;
    int flag=0;
    for (i=0;i<l1.size();i++)
    for (j=0;j<l2.size();j++)
    if (l1[i]==l2[j])
    {
        flag=0;
        for (int k=0;k<common_elements.size();k++)
        if (l1[i]==common_elements[k])
        {
            flag=1;
            break;
        }
        if (flag==0)
        {
            common_elements.push_back(l1[i]);
        }
    }
    sort(common_elements.begin(),common_elements.end());
    return common_elements;
}

