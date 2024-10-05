    sort(arr.begin(),arr.end());
    vector<int> v;
    for (int i=arr.size()-1;i>=0&&k>0;i--,k--)
    v.push_back(arr[i]);
    return v;
}


