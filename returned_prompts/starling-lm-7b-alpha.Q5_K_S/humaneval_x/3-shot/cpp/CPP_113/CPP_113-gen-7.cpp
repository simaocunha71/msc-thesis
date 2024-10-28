    vector<string> result;
    int i,j;
    int odd_count;
    for (i=0;i<lst.size();i++)
    {
        odd_count=0;
        for (j=0;j<lst[i].length();j++)
        if (lst[i][j]%2!=0)
        odd_count+=1;

        result.push_back("the number of odd elements "+
        to_string(odd_count)+"n the str"+to_string(odd_count)+"ng "+
        "of the "+to_string(odd_count)+"nput.");
    }
    return result;
}

