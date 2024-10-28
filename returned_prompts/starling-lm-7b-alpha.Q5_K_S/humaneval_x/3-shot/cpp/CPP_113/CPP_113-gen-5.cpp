    vector<string> output;
    int odd_count;
    int i;
    for (i=0;i<lst.size();i++)
    {
        odd_count=0;
        for (char c:lst[i])
        if (c%2!=0) odd_count+=1;
        stringstream ss;
        ss<<"the number of odd elements "<<odd_count<<'n'<<"the str"<<odd_count<<'n'<<"of the "<<odd_count<<'n'<<"nput.";
        string output_string=ss.str();
        output.push_back(output_string);
    }
    return output;
}



