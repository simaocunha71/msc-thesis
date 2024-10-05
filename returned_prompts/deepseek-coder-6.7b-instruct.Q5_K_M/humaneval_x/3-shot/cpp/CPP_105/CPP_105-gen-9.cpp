    vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> result;
    map<int, string> m;
    int i;
    for  (i=0;i<9;i++)
    m[i+1]=names[i];
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());
    for  (i=0;i<arr.size();i++)
    if  (m.count(arr[i]))
    result.push_back(m[arr[i]]);
    return result;
}


