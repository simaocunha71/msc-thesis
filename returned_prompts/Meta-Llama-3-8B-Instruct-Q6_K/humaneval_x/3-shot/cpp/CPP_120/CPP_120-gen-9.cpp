    vector<int> result;
    sort(arr.begin(),arr.end(),greater<int>());
    for(int i=0;i<k;i++)
    result.push_back(arr[i]);
    return result;
}  // O(n log n) time complexity, where n is the size of the input vector. The space complexity is O(k), where k is the size of the output vector.