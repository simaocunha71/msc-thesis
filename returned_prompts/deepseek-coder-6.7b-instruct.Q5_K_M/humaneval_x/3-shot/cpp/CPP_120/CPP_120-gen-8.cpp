    sort(arr.begin(),arr.end());
    vector<int> result(arr.end()-k,arr.end());
    reverse(result.begin(),result.end());
    return result;
}


