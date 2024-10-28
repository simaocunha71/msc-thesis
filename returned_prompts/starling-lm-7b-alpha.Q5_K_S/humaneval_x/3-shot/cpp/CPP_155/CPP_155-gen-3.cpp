    vector<int> result;
    string str=to_string(num);
    int even_count=0,odd_count=0;
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]%2==0)
        {
        even_count+=1;
        }
        else
        {
        odd_count+=1;
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);

    return result;
}


