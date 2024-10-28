    map<string,string> nums;
    nums["zero"]="0";
    nums["one"]="1";
    nums["two"]="2";
    nums["three"]="3";
    nums["four"]="4";
    nums["five"]="5";
    nums["six"]="6";
    nums["seven"]="7";
    nums["eight"]="8";
    nums["nine"]="9";

    vector<string> numbers_str;
    char chr;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr>='0' && chr<='9')
            numbers_str.push_back(nums[string(1,chr)]);
        else
            numbers_str.push_back(string(1,chr));
    }

    sort(numbers_str.begin(),numbers_str.end());
    string result;
    for (i=0;i<numbers_str.size();i++)
        result+=numbers_str[i];

    return result;
}


