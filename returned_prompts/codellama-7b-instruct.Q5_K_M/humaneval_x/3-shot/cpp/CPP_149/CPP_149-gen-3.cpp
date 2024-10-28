    vector<string> sorted_list;
    vector<int> lengths;
    vector<string> words;
    int i;
    for (i=0;i<lst.size();i++)
    {
        lengths.push_back(lst[i].length());
        words.push_back(lst[i]);
    }
    sort(lengths.begin(), lengths.end());
    for (i=0;i<lengths.size();i++)
    {
        int j;
        for (j=0;j<words.size();j++)
        {
            if (lengths[i]==words[j].length())
            sorted_list.push_back(words[j]);
        }
    }
    sort(sorted_list.begin(), sorted_list.end());
    return sorted_list;
}



