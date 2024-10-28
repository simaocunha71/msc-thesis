    vector<int> max_vec;
    vector<int> numbers_vec;
    int i,max_num;
    numbers_vec=numbers;
    max_num=numbers_vec[numbers_vec.size()-1];
    max_vec.push_back(max_num);
    for (i=numbers_vec.size()-2;i>=0;i--)
    {
        if (numbers_vec[i]>=max_num)
        {
            max_num=numbers_vec[i];
        }
        max_vec.push_back(max_num);
    }
    return max_vec;
}


