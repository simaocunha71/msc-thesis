    vector<int> result;
    string num_str=to_string(num);
    int i;
    for (i=0;i<num_str.length();i++)
    {
        if (num_str[i]%2==0)
        {
            result.push_back(1);
        }
        else
        {
            result.push_back(0);
        }
    }
    return result;
}


