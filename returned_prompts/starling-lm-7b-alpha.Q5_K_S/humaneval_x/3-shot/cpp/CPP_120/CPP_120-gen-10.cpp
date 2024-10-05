    vector<int> res;
    sort(arr.begin(),arr.end(),greater<int>());
    int i;
    for (i=0;i<k;i++)
    res.push_back(arr[i]);

    return res;
}



