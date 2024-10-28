    vector<string> output;
    map<char,int> odd_counts;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]%2==1)
            {
                odd_counts[lst[i][j]]+=1;
            }
        }
    }
    for (auto it=odd_counts.begin();it!=odd_counts.end();it++)
    {
        char current_char=it->first;
        int current_count=it->second;
        output.push_back(to_string(current_count));
        output.push_back(string(current_count,'o'));
        output.push_back(to_string(current_char));
    }
    return output;
}


