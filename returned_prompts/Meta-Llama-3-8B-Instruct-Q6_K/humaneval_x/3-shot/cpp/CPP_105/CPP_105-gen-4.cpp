    vector<string> result;
    if (arr.empty()) return result;
    vector<int> arr_to_sort;
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]>=1 && arr[i]<=9) arr_to_sort.push_back(arr[i]);
    }
    sort(arr_to_sort.begin(), arr_to_sort.end());
    reverse(arr_to_sort.begin(), arr_to_sort.end());
    map<int,string> num_to_str = {{1,"One"},{2,"Two"},{3,"Three"},{4,"Four"},{5,"Five"},{6,"Six"},{7,"Seven"},{8,"Eight"},{9,"Nine"}};
    for (int i=0;i<arr_to_sort.size();i++)
    {
        result.push_back(num_to_str[arr_to_sort[i]]);
    }
    return result;
}  // 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4 ms / 8.4 MB
// 4