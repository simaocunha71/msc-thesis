    int i;
    int sum=0;
    float ceil_num;
    for (i=0;i<lst.size();i++)
    {
        ceil_num=ceil(lst[i]);
        sum+=(ceil_num*ceil_num);
    }
    return sum;
}



