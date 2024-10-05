    vector<int> res;
    sort(arr.begin(),arr.end());
    for(int i=0;i<k;i++)
    {
        res.push_back(arr[arr.size()-1-i]);
    }
    return res;
}  // Time Complexity: O(n log n) for sorting. Space Complexity: O(k) for the result array.