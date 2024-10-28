    vector<int> sorted_arr;
    vector<int> temp_arr;

    int i,j;
    for (i=0;i<arr.size();i++)
    {
        temp_arr.push_back(arr[i]);
        sort(temp_arr.begin(),temp_arr.end());
    }
    return temp_arr;
}




