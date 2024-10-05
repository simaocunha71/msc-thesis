    vector<int> result;
    string num_str=to_string(num);
    int length=num_str.length();
    int even_count=0;
    int odd_count=0;
    int i;
    for (i=0;i<length;i++)
    {
        if (num_str[i]%2==0)
        even_count+=1;
        else
        odd_count+=1;
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}


