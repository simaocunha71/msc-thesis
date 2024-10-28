    string num_str=to_string(num);
    int even=0;
    int odd=0;
    for (int i=0;i<num_str.length();i++)
    {
        if (num_str[i]%2==0)
        even+=1;
        else
        odd+=1;
    }
    vector<int> result={even,odd};
    return result;
}






