    vector<int> result;
    int even_count=0;
    int odd_count=0;
    int i;
    for (i=1;i<=n;i++)
    {
        string number_str=to_string(i);
        if (number_str==string(number_str.rbegin(),number_str.rend()))
        {
            if (i%2==0)
            even_count+=1;
            else
            odd_count+=1;
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}



