    vector<string> result;
    int i,odd_count;
    for (i=0;i<lst.size();i++)
    {
        odd_count=0;
        for (char chr : lst[i])
        if (chr%2!=0)
        odd_count+=1;
        result.push_back("the number of odd elements "+to_string(odd_count)+"n the str"+to_string(i)+"ng "+to_string(i)+"n the "+to_string(i)+"nput.");
    }
    return result;
}



