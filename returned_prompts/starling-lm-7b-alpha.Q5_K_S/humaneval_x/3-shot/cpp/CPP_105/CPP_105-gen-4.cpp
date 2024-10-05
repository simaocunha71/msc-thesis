    vector<int> sorted;
    for (int i=0;i<arr.size();i++)
    if (arr[i]>=1 && arr[i]<=9)
    sorted.push_back(arr[i]);

    sort(sorted.begin(),sorted.end());
    reverse(sorted.begin(),sorted.end());

    vector<string> ret;
    map<int,string> mapper = {
    {1, "One"},
    {2, "Two"},
    {3, "Three"},
    {4, "Four"},
    {5, "Five"},
    {6, "Six"},
    {7, "Seven"},
    {8, "Eight"},
    {9, "Nine"}
    };

    for (int i=0;i<sorted.size();i++)
    ret.push_back(mapper[sorted[i]]);

    return ret;
}


