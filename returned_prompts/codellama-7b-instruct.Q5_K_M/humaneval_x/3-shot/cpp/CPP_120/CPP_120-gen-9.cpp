    vector<int> result;
    sort(arr.begin(),arr.end(),greater<int>());
    for (int i=0;i<k;i++)
        result.push_back(arr[i]);
    return result;
}


