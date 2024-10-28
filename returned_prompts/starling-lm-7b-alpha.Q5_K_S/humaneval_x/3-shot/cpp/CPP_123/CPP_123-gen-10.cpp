    vector<int> collatz_odd_nums;
    int i;
    int current_num=n;
    while (current_num!=1)
    {
        if (current_num%2==1)
        collatz_odd_nums.push_back(current_num);
        current_num=(current_num%2==1)?(current_num*3+1):(current_num/2);
    }
    sort(collatz_odd_nums.begin(), collatz_odd_nums.end());
    return collatz_odd_nums;
}



