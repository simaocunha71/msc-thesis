    int even_count=0;
    int odd_count=0;
    string str_num=to_string(num);
    int i;
    for (i=0;i<str_num.length();i++)
    {
        if (str_num[i]-'0'%2==0)
        {
            even_count+=1;
        }
        else
        {
            odd_count+=1;
        }
    }
    vector<int> result={even_count, odd_count};
    return result;
}


