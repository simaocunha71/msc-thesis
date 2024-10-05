    vector<string> result;
    int count;
    for(int i=0; i<lst.size(); i++)
    {
        string s = lst[i];
        count = 0;
        for(int j=0; j<s.size(); j++)
        {
            if ((s[j] - '0') % 2 != 0)
                count++;
        }
        string str = "the number of odd elements in the string " + to_string(count) + " of the input.";
        result.push_back(str);
    }
    return result;
}


