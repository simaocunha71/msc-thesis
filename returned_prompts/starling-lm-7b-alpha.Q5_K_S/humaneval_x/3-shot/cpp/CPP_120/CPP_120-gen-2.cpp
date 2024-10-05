    vector<int> result;
    sort(arr.begin(),arr.end());
    int i;
    for (i=0;i<k;i++)
    result.push_back(arr[arr.size()-i-1]);

    return result;
}



