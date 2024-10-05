    vector<int> max_rolling;
    int max_num=INT_MIN;
    for(int i=0;i<numbers.size();i++)
    {
        if(numbers[i]>max_num)
        {
            max_num=numbers[i];
        }
        max_rolling.push_back(max_num);
    }
    return max_rolling;
}  // This code is not working properly. It always returns the maximum number in the whole sequence, not the rolling maximum.


