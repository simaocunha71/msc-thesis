    vector<int> result;
    for (int i: l)
    {
        result.push_back(i+1);
    }
    return result;
}  // This will not work correctly for large numbers
// We need to use vector<int> instead of vector<long long int> for large numbers


