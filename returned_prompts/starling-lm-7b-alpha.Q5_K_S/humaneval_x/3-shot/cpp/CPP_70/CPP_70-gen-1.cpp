    sort(lst.begin(),lst.end());
    int i,n=lst.size();
    vector<int> result;
    for (i=0;i<n;i++)
    if (i%2==0)
    result.push_back(lst[i]);
    else
    result.push_back(lst[n-i-1]);
    return result;
}




