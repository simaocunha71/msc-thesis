    vector<int> result;
    string number_str=to_string(num);
    int i,j;
    for (i=0;i<number_str.length();i++)
    {
        if (number_str[i]-'0'%2==0)
            result.push_back(result.size()+1);
        else
            result.push_back(result.size());
    }
    return result;
}



