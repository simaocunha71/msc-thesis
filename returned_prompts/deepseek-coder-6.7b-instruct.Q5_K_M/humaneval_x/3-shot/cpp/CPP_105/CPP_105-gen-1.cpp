    vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    map<int, string> num_to_name;
    for(int i = 0; i<9; i++)
        num_to_name[i+1] = names[i];
    vector<int> valid_nums;
    for(auto num : arr)
        if(num_to_name.count(abs(num)))
            valid_nums.push_back(abs(num));
    sort(valid_nums.begin(), valid_nums.end());
    reverse(valid_nums.begin(), valid_nums.end());
    vector<string> result;
    for(auto num : valid_nums)
        result.push_back(num_to_name[num]);
    return result;
}


A: Here are the solutions in Python:

