    vector<int> odd;
    vector<int> even;
    for (int i=0;i<lst.size();i++)
    if (lst[i]%2==0)
    even.push_back(lst[i]);
    else
    odd.push_back(lst[i]);
    sort(even.begin(),even.end());
    sort(odd.begin(),odd.end());
    vector<int> out;
    out.push_back(even[0]);
    out.push_back(even[even.size()-1]);
    out.push_back(odd[0]);
    out.push_back(odd[odd.size()-1]);
    return out;
}

