    vector<string> output;
    for (int i=0;i<lst.size();i++)
    {
        int count=0;
        for (int j=0;j<lst[i].length();j++)
        {
            if ((lst[i][j]-48)%2==1)
            {
                count+=1;
            }
        }
        output.push_back("the number of odd elements " + to_string(count) + "n the str" + to_string(count) + "ng " + to_string(count) + " of the " + to_string(count) + "nput.");
    }
    return output;
}

