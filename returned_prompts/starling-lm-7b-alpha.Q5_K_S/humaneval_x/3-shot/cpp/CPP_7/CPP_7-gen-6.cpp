    vector<string> res;
    for (int i=0;i<strings.size();i++)
    {
        if (strings[i].find(substring)!=string::npos)
        {
            res.push_back(strings[i]);
        }
    }
    return res;
}


