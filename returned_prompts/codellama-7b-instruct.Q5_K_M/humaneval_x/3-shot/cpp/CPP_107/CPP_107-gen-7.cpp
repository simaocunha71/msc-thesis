    vector<int> all_nums;
    int i;
    string temp;
    int temp_num;
    for (i=1;i<=n;i++)
    {
        temp=to_string(i);
        if (temp==temp_reverse(temp))
        {
            temp_num=stoi(temp);
            if (temp_num%2==0)
            all_nums[0]++;
            else
            all_nums[1]++;
        }
    }
    return all_nums;
}


