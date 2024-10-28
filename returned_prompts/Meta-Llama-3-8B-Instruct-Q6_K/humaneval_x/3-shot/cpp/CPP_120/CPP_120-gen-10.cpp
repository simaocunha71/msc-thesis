    vector<int> result(arr.begin(),arr.begin()+k);
    sort(result.begin(),result.end(),greater<int>());
    return result;
}