    sort(lst.begin(),lst.end());
    vector<int> output;
    int i=0;
    while (i<lst.size())
    {
        output.push_back(lst[i]);
        i+=2;
    }
    i=1;
    while (i<lst.size())
    {
        output.push_back(lst[i]);
        i+=2;
    }
    return output;
}

