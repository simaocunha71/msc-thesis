    vector<string> all_odds;
    vector<string> all_evens;
    vector<string> all_lst;
    string chr;
    int i;
    for (i=0;i<lst.size();i++)
    {
        chr=lst[i];
        if (chr.length()%2==1)
        all_odds.push_back(chr);
        else
        all_evens.push_back(chr);
    }
    sort(all_odds.begin(),all_odds.end());
    sort(all_evens.begin(),all_evens.end());
    all_lst=all_evens;
    for (i=0;i<all_odds.size();i++)
    all_lst.push_back(all_odds[i]);
    return all_lst;
}



