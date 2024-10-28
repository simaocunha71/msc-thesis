    vector<string> all_counts;
    int i,j;
    int count;
    string output;
    int chr;
    for (i=0;i<lst.size();i++)
    {
        count=0;
        output="";
        for (j=0;j<lst[i].length();j++)
        {
            chr=int(lst[i][j]);
            if (chr%2==1)
                count+=1;
        }
        output="the number of odd elements "+to_string(count)+"n the str"+to_string(count)+"ng "+to_string(count)+" of the "+to_string(count)+"nput.";
        all_counts.push_back(output);
    }
    return all_counts;
}

