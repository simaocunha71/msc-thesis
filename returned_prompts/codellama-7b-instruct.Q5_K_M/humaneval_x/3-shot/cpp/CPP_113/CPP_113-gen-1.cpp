    map<int,int> odd_counts;
    int i;
    for (i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].length();j++)
    if (lst[i][j]%2!=0)
    odd_counts[i]++;

    vector<string> result;
    for (map<int,int>::iterator it=odd_counts.begin();it!=odd_counts.end();it++)
    result.push_back("the number of odd elements "+to_string(it->second)+"n the str"+to_string(it->first)+"ng "+to_string(it->first)+" of the "+to_string(it->first)+"nput.");

    return result;
}



