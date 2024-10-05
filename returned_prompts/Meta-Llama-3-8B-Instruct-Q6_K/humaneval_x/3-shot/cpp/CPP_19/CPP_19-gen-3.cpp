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
    string result;
    vector<string> nums;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        if (numbers[i]==' ')
        continue;
        else
        {
            string num;
            while (i<numbers.length() && numbers[i] != ' ')
            {
                num+=numbers[i];
                i++;
            }
            i--;
            nums.push_back(num);
        }
    }
    sort(nums.begin(),nums.end(),[&num_map](string a, string b)
    {
        return num_map[a] < num_map[b];
    });
    for (i=0;i<nums.size();i++)
    {
        result+=nums[i];
        if (i<nums.size()-1)
        result+=' ';
    }
    return result;
} // end of sort_numbers() function
} // end of namespace std

