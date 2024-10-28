    sort(arr.begin(),arr.end());
    vector<int> all_k;
    for (int i=arr.size()-1;i>k-1;i--)
    all_k.push_back(arr[i]);
    return all_k;
}

