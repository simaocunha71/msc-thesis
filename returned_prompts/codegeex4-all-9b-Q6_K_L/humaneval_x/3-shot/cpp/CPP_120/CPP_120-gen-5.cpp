    sort(arr.begin(), arr.end());
    int i;
    vector<int> max_k;
    for (i=arr.size()-k;i<arr.size();i++)
        max_k.push_back(arr[i]);
    return max_k;
}

