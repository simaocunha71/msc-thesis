    map<string, int> num_map;
    num_map["zero"]=0;
    num_map["one"]=1;
    num_map["two"]=2;
    num_map["three"]=3;
    num_map["four"]=4;
    num_map["five"]=5;
    num_map["six"]=6;
    num_map["seven"]=7;
    num_map["eight"]=8;
    num_map["nine"]=9;
    vector<string> nums;
    string word;
    for (int i=0;i<numbers.length();i++)
    {
        if (numbers[i]==' ')
        {
            nums.push_back(word);
            word="";
        }
        else
        {
            word+=numbers[i];
        }
    }
    nums.push_back(word);
    sort(nums.begin(), nums.end(), [](string a, string b) {
        return num_map[a]<num_map[b];
    });
    string sorted_nums="";
    for (int i=0;i<nums.size();i++)
    {
        if (i>0)
        {
            sorted_nums+=" ";
        }
        sorted_nums+=nums[i];
    }
    return sorted_nums;
}