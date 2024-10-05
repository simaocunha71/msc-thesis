    vector<int> array_copy = array;
    int sum = array[0] + array[array.size()-1];
    if (sum % 2 == 0)
        sort(array_copy.begin(), array_copy.end(), greater<int>());
    else
        sort(array_copy.begin(), array_copy.end());
    return array_copy;
}