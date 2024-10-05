    map<string, int> num_map;
    num_map["zero"] = 0;
    num_map["one"] = 1;
    num_map["two"] = 2;
    num_map["three"] = 3;
    num_map["four"] = 4;
    num_map["five"] = 5;
    num_map["six"] = 6;
    num_map["seven"] = 7;
    num_map["eight"] = 8;
    num_map["nine"] = 9;
    vector<string> nums;
    string curr_num;
    for (int i=0;i<numbers.length();i++)
    {
        if (numbers[i]==' ')
        {
            nums.push_back(curr_num);
            curr_num="";
        }
        else
        {
            curr_num+=numbers[i];
        }
    }
    nums.push_back(curr_num);
    sort(nums.begin(), nums.end(), 
    [](const string& a, const string& b)->bool 
    { 
        return num_map[a] < num_map[b]; 
    });
    string result;
    for (int i=0;i<nums.size();i++)
    {
        if (i>0) result+=' ';
        result+=nums[i];
    }
    return result;
}  //  This function takes a string of numbers in the range 0-9, separated by spaces, and returns a string with those numbers in sorted order
// It first creates a map of the numbers and their corresponding integer values. Then it splits the input string into individual numbers, 
// sorts them using a lambda function that compares the values in the map, and finally joins them back together into a single string.  //


