    vector<int> result;
    string num_string=to_string(num);
    int even=0;
    int odd=0;
    int i;
    for (i=0;i<num_string.length();i++)
    {
        if (num_string[i]%2==0)
        even+=1;
        else
        odd+=1;
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}


