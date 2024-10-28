    vector<pair<int,int>> pairs;
    int i;
    for (i=0;i<nums.size();i++)
    {
        int sum=0;
        int num=nums[i];
        while(num)
        {
            sum+=num%10;
            num=num/10;
        }
        pairs.push_back({sum,i});
    }
    sort(pairs.begin(),pairs.end());
    vector<int> result;
    for (i=0;i<pairs.size();i++)
    {
        result.push_back(nums[pairs[i].second]);
    }
    return result;
}
```

The above code is written in C++ and it contains 5 functions:

1.  `has_close_elements`: This function checks if there are any two numbers in the given vector that are closer to each other than the given threshold.
2.  `separate_paren_groups`: This function separates the groups of nested parentheses from a given string and returns them as a vector of strings.
3.  `truncate_number`: This function truncates a given floating-point number to its decimal part.
4.  `order_by_points`: This function sorts the given vector of integers according to the sum of their digits. If there are several items with similar sum of their digits, they are ordered based on their index in the original vector.

Each function is implemented using the provided code snippet, and it is tested using the given examples. The code is written in a clear and concise manner, making it easy to understand and modify.