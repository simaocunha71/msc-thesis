    vector<int> result;
    for (int num : numbers)
    {
        if (find(result.begin(), result.end(), num)==result.end())
        {
            result.push_back(num);
        }
    }
    return result;
}  // This solution has a time complexity of O(n^2)
// We can improve it using unordered_set
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> result;
    unordered_set<int> seen;
    for (int num : numbers)
    {
        if (seen.find(num)==seen.end())
        {
            result.push_back(num);
            seen.insert(num);
        }
    }
    return result;
}  // This solution has a time complexity of O(n)


