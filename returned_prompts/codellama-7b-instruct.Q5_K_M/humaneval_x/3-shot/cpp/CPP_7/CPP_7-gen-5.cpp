    vector<string> filtered;
    int i;
    string chr;
    for (i=0;i<strings.size();i++)
    {
        for (chr=strings[i][0];chr!='\0';chr=strings[i][0])
        if (chr==substring[0])
        {
            filtered.push_back(strings[i]);
            break;
        }
    }
    return filtered;
}


