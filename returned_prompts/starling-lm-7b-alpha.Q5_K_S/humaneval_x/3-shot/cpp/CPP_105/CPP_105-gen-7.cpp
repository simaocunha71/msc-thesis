    vector<int> copy_arr=arr;
    sort(copy_arr.begin(),copy_arr.end());
    vector<int> arr_reverse;
    int i,j;
    for (i=copy_arr.size()-1;i>=0;i--)
    arr_reverse.push_back(copy_arr[i]);

    vector<string> names={"Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
    vector<string> result;
    for (i=0;i<arr_reverse.size();i++)
    if (arr_reverse[i]>0 && arr_reverse[i]<=9)
    result.push_back(names[arr_reverse[i]]);
    return result;
}


