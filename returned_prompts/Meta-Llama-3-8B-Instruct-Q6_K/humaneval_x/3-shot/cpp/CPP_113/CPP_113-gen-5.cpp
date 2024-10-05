    vector<string> result;
    int i;
    map<string, int> odd_count_map;
    for (i=0;i<lst.size();i++)
    {
        int j;
        int odd_count=0;
        for (j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]-'0'%2==1)
                odd_count++;
        }
        odd_count_map.insert(pair<string, int>(lst[i], odd_count));
    }
    for (i=0;i<lst.size();i++)
    {
        result.push_back("the number of odd elements "+to_string(odd_count_map[lst[i]])+"n the str"+to_string(i+1)+"ng "+lst[i]+" of the "+to_string(i+1)+"nput.");
    }
    return result;
}
