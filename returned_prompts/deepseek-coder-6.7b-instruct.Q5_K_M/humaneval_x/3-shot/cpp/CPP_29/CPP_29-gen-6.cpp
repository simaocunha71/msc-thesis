    vector<string> result;
    int i;
    for(i=0; i<strings.size(); i++)
    {
        if(strings[i].substr(0, prefix.size()) == prefix)
        {
            result.push_back(strings[i]);
        }
    }
    return result;
}


