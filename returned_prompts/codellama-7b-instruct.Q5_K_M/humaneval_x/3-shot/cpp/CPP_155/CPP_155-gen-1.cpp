    vector<int> result;
    string num_str=to_string(num);
    int even=0;
    int odd=0;
    int i;
    for(i=0;i<num_str.length();i++)
    {
        if (num_str[i]=='0' || num_str[i]=='2' || num_str[i]=='4' || num_str[i]=='6' || num_str[i]=='8')
        {
            even++;
        }
        else
        {
            odd++;
        }
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}


