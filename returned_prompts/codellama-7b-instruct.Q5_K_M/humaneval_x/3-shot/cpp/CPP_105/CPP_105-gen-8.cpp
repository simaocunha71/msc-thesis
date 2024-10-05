    vector<string> names;
    map<int,string> num_to_name = {
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
    sort(arr.begin(),arr.end());
    reverse(arr.begin(),arr.end());
    for (int i=0;i<arr.size();i++)
    {
    if (num_to_name.find(arr[i])!=num_to_name.end())
        names.push_back(num_to_name[arr[i]]);
    }
    return names;
}

