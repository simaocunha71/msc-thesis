    vector<string> result;
    string temp;
    int i;
    for (i=0;i<strings.size();i++)
    {
        temp=strings[i];
        if (temp.find(prefix,0)==0)
        result.push_back(temp);
    }
    return result;
}



