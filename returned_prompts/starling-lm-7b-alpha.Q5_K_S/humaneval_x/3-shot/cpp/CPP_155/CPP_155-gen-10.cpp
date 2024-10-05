    vector<int> counts;
    string number_str=to_string(num);
    int i,count_odd=0,count_even=0;
    for (i=0;i<number_str.length();i++)
    {
        if (number_str[i]%2==0)
        {
        count_even+=1;
        }
        else
        {
        count_odd+=1;
        }
    }
    counts.push_back(count_even);
    counts.push_back(count_odd);
    return counts;
}




