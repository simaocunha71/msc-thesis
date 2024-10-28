    vector<int> result;
    int i,count_even=0,count_odd=0;
    string s=to_string(abs(num));
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='0'||s[i]=='2'||s[i]=='4'||s[i]=='6'||s[i]=='8')
            count_even+=1;
        else
            count_odd+=1;
    }
    result.push_back(count_odd);
    result.push_back(count_even);
    return result;
}



