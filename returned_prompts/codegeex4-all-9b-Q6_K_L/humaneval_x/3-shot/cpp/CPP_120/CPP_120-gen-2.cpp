    sort(arr.begin(),arr.end());
    vector<int> max_k;
    for (int i=arr.size()-1;i>=0;i--)
    {
        if (k==0) break;
        max_k.push_back(arr[i]);
        k--;
    }
    return max_k;
}

