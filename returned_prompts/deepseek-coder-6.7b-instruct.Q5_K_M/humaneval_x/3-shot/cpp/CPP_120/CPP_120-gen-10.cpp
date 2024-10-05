    sort(arr.begin(), arr.end());
    vector<int> res(arr.end() - k, arr.end());
    reverse(res.begin(), res.end());
    return res;
}


