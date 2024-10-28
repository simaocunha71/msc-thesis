    vector<string> result;
    for (int i=0;i<lst.size();i++)
    {
        string s=lst[i];
        int count=0;
        for (int j=0;j<s.length();j++)
        {
            if (s[j]%2!=0)
                count++;
        }
        result.push_back("the number of odd elements "+to_string(count)+"n the str"+to_string(count)+"ng "+to_string(count)+" of the "+to_string(count)+"nput.");
    }
    return result;
}
