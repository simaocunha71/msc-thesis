    map<string,int> number_map;
    string number;
    int i,j;
    for (i=0;i<numbers.length();i++)
    {
        number=numbers[i];
        if (number_map.find(number)==number_map.end())
        number_map[number]=1;
        else
        number_map[number]+=1;
    }
    string sorted_numbers="";
    vector<pair<string,int>> number_pairs;
    for (auto it=number_map.begin();it!=number_map.end();it++)
    {
    number_pairs.push_back(pair<string,int>(it->first,it->second));
    }
    for (i=0;i<number_pairs.size();i++)
    {
        for (j=0;j<number_pairs[i].second;j++)
        sorted_numbers+=number_pairs[i].first;
    }
    return sorted_numbers;
}


