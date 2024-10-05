    vector<string> odd_only;
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==1)
    odd_only.push_back(lst[i]);

    sort(odd_only.begin(), odd_only.end(), [](string a, string b) { return a.length() < b.length(); });

    vector<string> sorted_lst;
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    sorted_lst.push_back(lst[i]);

    sort(sorted_lst.begin(), sorted_lst.end());
    odd_only.insert(odd_only.end(), sorted_lst.begin(), sorted_lst.end());

    return odd_only;
}


