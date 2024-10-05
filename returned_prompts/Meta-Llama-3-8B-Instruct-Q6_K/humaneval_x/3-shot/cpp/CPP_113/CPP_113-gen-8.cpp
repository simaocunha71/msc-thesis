    vector<string> result;
    for (int i=0;i<lst.size();i++)
    {
        string temp=lst[i];
        int count=0;
        for (int j=0;j<temp.length();j++)
        {
            if (temp[j]%2!=0)
            {
                count++;
            }
        }
        result.push_back(string("the number of odd elements ") + to_string(count) + "n the str" + to_string(i+1) + "ng " + to_string(i+1) + " of the " + to_string(i+1) + "nput.");
    }
    return result;
}
