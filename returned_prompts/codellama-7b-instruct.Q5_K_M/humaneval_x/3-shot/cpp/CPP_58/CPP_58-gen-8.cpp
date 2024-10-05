    vector<int> l3;
    vector<int> l4;
    l3=l1;
    l4=l2;
    sort(l3.begin(),l3.end());
    sort(l4.begin(),l4.end());
    vector<int> result;
    int i;
    for (i=0;i<l3.size();i++)
    {
        int j;
        for (j=0;j<l4.size();j++)
        {
            if (l3[i]==l4[j])
            result.push_back(l3[i]);
        }
    }
    return result;
}



