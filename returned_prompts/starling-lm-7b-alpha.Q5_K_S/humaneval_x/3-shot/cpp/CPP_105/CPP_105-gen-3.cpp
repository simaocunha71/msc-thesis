    vector<int> tmp;
    vector<int> tmp2;
    for (int i=0;i<arr.size();i++)
    if (arr[i]>=1 && arr[i]<=9)
    {
        tmp.push_back(arr[i]);
    }
    sort(tmp.begin(),tmp.end());
    reverse(tmp.begin(),tmp.end());
    for (int i=0;i<tmp.size();i++)
    {
        tmp2.push_back(tmp[i]);
        map<int,string> nums={
            {0,"Zero"},
            {1,"One"},
            {2,"Two"},
            {3,"Three"},
            {4,"Four"},
            {5,"Five"},
            {6,"Six"},
            {7,"Seven"},
            {8,"Eight"},
            {9,"Nine"}
        };
        tmp2[i]=nums[tmp[i]];
    }
    return tmp2;
}


