    int count=0;
    vector<int> left;
    vector<int> right;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (i<arr.size()/2)
        left.push_back(arr[i]);
        else
        right.push_back(arr[i]);
    }
    for (i=0;i<left.size();i++)
    {
        if (left[i]!=right[left.size()-i-1])
        count++;
    }
    return count;
}