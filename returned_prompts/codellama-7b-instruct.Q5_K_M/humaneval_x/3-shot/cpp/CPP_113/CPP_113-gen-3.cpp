    vector<string> output;
    map<string,int> odd_count_map;
    int i;
    for (i=0;i<lst.size();i++)
    {
        string current_string=lst[i];
        for (int j=0;j<current_string.length();j++)
        {
            if (int(current_string[j])%2==1)
            {
            odd_count_map[current_string]=odd_count_map[current_string]+1;
            }
        }
    }
    for (i=0;i<lst.size();i++)
    {
        string current_string=lst[i];
        output.push_back("the number of odd elements "+odd_count_map[current_string]+"n the str"+odd_count_map[current_string]+"ng "+i+" of the "+odd_count_map[current_string]+"nput." );
    }
    return output;
}



