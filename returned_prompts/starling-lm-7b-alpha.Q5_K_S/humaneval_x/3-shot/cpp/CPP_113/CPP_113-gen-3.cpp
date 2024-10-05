    vector<string> result;
    int i;
    for (i=0;i<lst.size();i++)
    {
        result.push_back("the number of odd elements "+
        to_string(count_if(lst[i].begin(),lst[i].end(),
        [](char c){return c%2!=0;}))+" in the "+
        to_string(lst[i].size())+"n the str"+to_string(lst[i].size())+"ng "+
        "of the "+to_string(lst.size())+"nput.");
    }
    return result;
}

