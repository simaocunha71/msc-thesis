    vector<string> filtered;
    int i,j;
    int flag;
    for (i=0;i<strings.size();i++)
    {
        flag=0;
        for (j=0;j<substring.length();j++)
        {
            if (strings[i][j]==substring[j])
            flag+=1;
        }
        if (flag==substring.length())
        filtered.push_back(strings[i]);
    }
    return filtered;
}

