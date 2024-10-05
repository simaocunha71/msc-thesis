    vector<string> all;
    int i;
    for (i=0;i<words.size();i++)
    {
        string temp=words[i];
        sort(temp.begin(),temp.end());
        temp.erase(unique(temp.begin(),temp.end()),temp.end());
        all.push_back(temp);
    }
    sort(all.begin(),all.end());
    return all[all.size()-1];
}


