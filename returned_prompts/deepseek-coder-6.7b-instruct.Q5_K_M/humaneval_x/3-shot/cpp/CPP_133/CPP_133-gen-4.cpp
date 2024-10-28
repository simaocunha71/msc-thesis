    int sum=0;
    for  (int i=0;i<lst.size();i++)
    {
        int rounded_number=ceil(lst[i]);
        sum+=rounded_number*rounded_number;
    }
    return sum;
}


