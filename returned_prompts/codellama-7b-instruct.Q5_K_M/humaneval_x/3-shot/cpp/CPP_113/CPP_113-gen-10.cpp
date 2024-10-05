    vector<string> answer;
    map<string, int> odd_map;
    for (int i=0;i<lst.size();i++)
    {
        string current_string=lst[i];
        int current_size=current_string.size();
        for (int j=0;j<current_size;j++)
        {
            string current_digit=current_string[j];
            if (current_digit>='5')
            {
                odd_map[current_digit]=odd_map[current_digit]+1;
            }
        }
    }
    for (auto it=odd_map.begin();it!=odd_map.end();it++)
        answer.push_back(to_string(it->second));
    return answer;
}



