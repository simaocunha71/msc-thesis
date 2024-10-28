    vector<string> sorted_strs;
    vector<int> sorted_nums;
    map<int, string> num_to_str;
    map<int, string>::iterator it;
    for (int i=1;i<=9;i++)
    num_to_str[i]="";
    num_to_str[1]="One";
    num_to_str[2]="Two";
    num_to_str[3]="Three";
    num_to_str[4]="Four";
    num_to_str[5]="Five";
    num_to_str[6]="Six";
    num_to_str[7]="Seven";
    num_to_str[8]="Eight";
    num_to_str[9]="Nine";
    for (int i=0;i<arr.size();i++)
    {
        if (num_to_str[arr[i]]=="")
        sorted_nums.push_back(arr[i]);
    }
    sort(sorted_nums.begin(), sorted_nums.end());
    reverse(sorted_nums.begin(), sorted_nums.end());
    for (int i=0;i<sorted_nums.size();i++)
    {
        it=num_to_str.find(sorted_nums[i]);
        if (it!=num_to_str.end())
        sorted_strs.push_back(num_to_str[sorted_nums[i]]);
    }
    return sorted_strs;
}


