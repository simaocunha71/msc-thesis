    vector<int> max_nums;
    int max_num;
    int i,j;
    max_num=numbers[0];
    max_nums.push_back(max_num);
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>max_num){
            max_num=numbers[i];
        }
        max_nums.push_back(max_num);
    }
    return max_nums;
}


