    vector<string> result;
    for (int i=0;i<lst.size();i++)
    {
        int count=0;
        for (char c:lst[i])
        {
            if (c-'0'%2==1)
                count++;
        }
        result.push_back("the number of odd elements "+to_string(count)+" in the string "+to_string(i+1)+" of the input.");
    }
    return result;
}