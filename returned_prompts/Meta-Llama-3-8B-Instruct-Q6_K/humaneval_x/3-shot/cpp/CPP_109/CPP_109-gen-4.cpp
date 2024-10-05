    int i;
    vector<int> copy_arr = arr;
    for (i=0;i<arr.size();i++)
    {
        copy_arr.push_back(arr[i]);
        sort(copy_arr.begin(), copy_arr.end());
        if (copy_arr==arr)
        return true;
        copy_arr.erase(copy_arr.begin(), copy_arr.begin()+arr.size());
    }
    return false;
}   


