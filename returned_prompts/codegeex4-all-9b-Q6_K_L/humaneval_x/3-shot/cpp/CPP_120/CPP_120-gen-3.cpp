    sort(arr.begin(),arr.end());
    vector<int> max_arr;
    int i;
    for (i=arr.size()-k;i<arr.size();i++)
    max_arr.push_back(arr[i]);
    return max_arr;
}

