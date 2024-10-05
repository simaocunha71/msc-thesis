    vector<string> only_even,sorted_list;
    string word;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        word=lst[i];
        if (word.length()%2==0)
        {
        sorted_list.push_back(word);
        }
        else
        {
        only_even.push_back(word);
        }
    }
    sort(sorted_list.begin(),sorted_list.end(),[](string a, string b){return a.length()<b.length();});
    sort(only_even.begin(),only_even.end());
    for (i=0;i<only_even.size();i++)
    {
        sorted_list.push_back(only_even[i]);
    }
    return sorted_list;
}

